from django.shortcuts import render, redirect
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required
from .models import CheckOut
from datetime import datetime
from product.models import product
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

@login_required(login_url='userlogin')
def CheckoutViews(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, 'No items found in cart. Please visit our shop page to add products.')
        return redirect('shop')
        
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        product_qty = request.POST.get('product_qty')
        products_id = request.POST.get('products_id')
        username = request.POST.get('username')
        
        # Calculate order total
        OrderPrice = 0.0
        values = list(cart.values())
        for item in values:
            OrderPrice += float(item['price']) * float(item['quantity'])
        
        # Add shipping cost
        OrderPrice += 10.0

        try:
            data = CheckOut(
                first_name=fname,
                last_name=lname,
                checkout_email=email,
                mobile=mobile,
                address=address,
                product_qty=product_qty,
                products_id=products_id,
                username=username,
                Payment_type="Pending",  # Set initial payment type as Pending
                Payment_status="Pending",
                OrderPrice=str(OrderPrice)
            )
            data.save()
            
            # Store order ID in session for payment processing
            request.session['order_id'] = data.id
            
            # Redirect to payment method page
            return redirect('payment_method')
                
        except Exception as e:
            messages.error(request, f'An error occurred while processing your order: {str(e)}')
            return redirect('checkout')

    # Calculate cart total for display
    cart_total = 0.0
    for item in cart.values():
        cart_total += float(item['price']) * float(item['quantity'])

    context = {
        'cart_total': cart_total,
    }
    return render(request, "checkout.html", context)

@login_required(login_url='userlogin')
def payment_method(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, 'No items found in cart. Please visit our shop page to add products.')
        return redirect('shop')
    
    # Calculate cart total for display
    cart_total = 0.0
    for item in cart.values():
        cart_total += float(item['price']) * float(item['quantity'])
    
    context = {
        'cart_total': cart_total,
    }
    return render(request, "payment_method.html", context)

@login_required(login_url='userlogin')
def online_payment(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, 'No items found in cart. Please visit our shop page to add products.')
        return redirect('shop')
    
    if request.method == "POST":
        order_id = request.session.get('order_id')
        try:
            order = CheckOut.objects.get(id=order_id)
            
            # Get card details
            card_holder = request.POST.get('card_holder')
            card_number = request.POST.get('card_number')
            expiry_month = request.POST.get('expiry_month')
            expiry_year = request.POST.get('expiry_year')
            cvv = request.POST.get('cvv')
            
            # Basic card validation
            if not all([card_holder, card_number, expiry_month, expiry_year, cvv]):
                messages.error(request, 'Please provide all card details.')
                return redirect('online_payment')
            
            # Here you would typically integrate with a payment gateway
            # For now, we'll simulate a successful payment
            try:
                # Store cart data for invoice before clearing
                cart_data = request.session.get('cart', {})
                
                # Update quantities after successful payment
                values = list(cart_data.values())
                for item in values:
                    productObj = product.objects.get(id=item['product_id'])
                    productObj.qty -= float(item['quantity'])
                    productObj.save()
                
                # Clear the cart
                request.session['cart'] = {}
                order.Payment_status = "Paid"  # Mark as paid for online payments
                order.save()
                messages.success(request, 'Payment successful! Your order has been placed.')
                return render(request, "invoice.html", {
                    "data": order,
                    "cart": cart_data,
                    "cart_total": sum(float(item['price']) * float(item['quantity']) for item in cart_data.values())
                })
            except Exception as e:
                messages.error(request, f'Payment processing failed: {str(e)}')
                return redirect('online_payment')
                
        except CheckOut.DoesNotExist:
            messages.error(request, 'Order not found. Please try again.')
            return redirect('checkout')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('checkout')
    
    # Calculate cart total for display
    cart_total = 0.0
    for item in cart.values():
        cart_total += float(item['price']) * float(item['quantity'])
    
    context = {
        'cart': cart,
        'cart_total': cart_total,
    }
    return render(request, "Payment.html", context)

@login_required(login_url='userlogin')
def process_payment(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, 'No items found in cart. Please visit our shop page to add products.')
        return redirect('shop')
        
    if request.method == "POST":
        payment_method = request.POST.get('payment_method')
        order_id = request.session.get('order_id')
        
        try:
            order = CheckOut.objects.get(id=order_id)
            
            # Validate payment method
            if payment_method not in ["COD", "ONLINE"]:
                messages.error(request, 'Invalid payment method selected. Please try again.')
                return redirect('payment_method')
            
            # Update order with payment method
            order.Payment_type = "COD" if payment_method == "COD" else "Online"
            order.Payment_status = "Pending"
            order.save()
            
            # Validate product quantities before processing
            cart = request.session.get('cart', {})
            values = list(cart.values())
            for item in values:
                try:
                    productObj = product.objects.get(id=item['product_id'])
                    if productObj.qty < float(item['quantity']):
                        messages.error(request, f'Sorry, {productObj.name} is out of stock.')
                        return redirect('checkout')
                except product.DoesNotExist:
                    messages.error(request, 'Some products in your cart are no longer available.')
                    return redirect('checkout')
            
            # Process payment based on method
            if payment_method == "COD":
                # For COD, just update quantities and show success
                for item in values:
                    productObj = product.objects.get(id=item['product_id'])
                    productObj.qty -= float(item['quantity'])
                    productObj.save()
                
                # Store cart data for invoice before clearing
                cart_data = request.session.get('cart', {})
                
                # Clear the cart
                request.session['cart'] = {}
                messages.success(request, 'Order placed successfully! You will receive your order soon.')
                return render(request, "invoice.html", {
                    "data": order,
                    "cart": cart_data,
                    "cart_total": sum(float(item['price']) * float(item['quantity']) for item in cart_data.values())
                })
            else:
                # For online payment, redirect to payment page
                return redirect('online_payment')
                
        except CheckOut.DoesNotExist:
            messages.error(request, 'Order not found. Please try again.')
            return redirect('checkout')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('checkout')
    
    return redirect('payment_method')

@login_required(login_url='userlogin')
def invoice(request):
    try:
        # Get order ID from session
        order_id = request.session.get('order_id')
        if not order_id:
            messages.error(request, 'No order found. Please complete the checkout process.')
            return redirect('checkout')
            
        # Get order data
        order = CheckOut.objects.get(id=order_id)
        
        # Handle different payment types
        if order.Payment_type == "COD":
            if order.Payment_status == "Pending":
                messages.info(request, 'For Cash on Delivery orders, the invoice will be available after delivery and payment completion.')
                return render(request, "order_success.html", {"order": order})
            elif order.Payment_status == "Paid":
                messages.success(request, 'Payment received. Here is your invoice.')
        else:  # Online payment
            if order.Payment_status == "Pending":
                messages.warning(request, 'Payment is still pending. Please complete the payment to view the invoice.')
                return redirect('payment_method')
            elif order.Payment_status == "Paid":
                messages.success(request, 'Payment successful. Here is your invoice.')
        
        # Calculate total from cart items
        cart = request.session.get('cart', {})
        total = 0.0
        for item in cart.values():
            total += float(item['price']) * float(item['quantity'])
        
        # Add shipping cost
        total += 10.0
        
        context = {
            'total': total,
            'data': order,
            'shipping_cost': 10.0,
            'payment_status': order.Payment_status,
            'payment_type': order.Payment_type
        }
        return render(request, "invoice.html", context)
        
    except CheckOut.DoesNotExist:
        messages.error(request, 'Order not found. Please try again.')
        return redirect('checkout')
    except Exception as e:
        messages.error(request, f'An error occurred while generating the invoice: {str(e)}')
        return redirect('checkout')

@login_required(login_url='userlogin')
def mark_order_paid(request, order_id):
    try:
        order = CheckOut.objects.get(id=order_id)
        
        # Only allow marking COD orders as paid
        if order.Payment_type != "COD":
            messages.error(request, 'This order cannot be marked as paid through this method.')
            return redirect('mainpage')
            
        # Update payment status
        order.Payment_status = "Paid"
        order.save()
        
        messages.success(request, 'Order has been marked as paid. You can now view the invoice.')
        
        # Redirect to invoice page
        request.session['order_id'] = order.id
        return redirect('invoice')
        
    except CheckOut.DoesNotExist:
        messages.error(request, 'Order not found.')
        return redirect('mainpage')
    except Exception as e:
        messages.error(request, 'An error occurred while updating the order.')
        return redirect('mainpage')