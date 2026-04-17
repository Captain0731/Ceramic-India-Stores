class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if cart is None:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'product_id': product.id,
                'name': product.name,
                'price': str(product.price),
                'quantity': 0,
                'image': product.image.url if getattr(product, 'image', None) else '',
            }

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def decrement(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] -= quantity
            if self.cart[product_id]['quantity'] <= 0:
                del self.cart[product_id]
            self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.session.pop('cart', None)
        self.save()

    def save(self):
        self.session.modified = True
