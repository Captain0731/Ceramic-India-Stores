from django.urls import path
from . import views

urlpatterns = [
    path('', views.CheckoutViews, name="checkout"),
    path('payment-method/', views.payment_method, name="payment_method"),
    path('process-payment/', views.process_payment, name="process_payment"),
    path('online-payment/', views.online_payment, name="online_payment"),
    path('invoice/', views.invoice, name="invoice"),
    path('mark-order-paid/<int:order_id>/', views.mark_order_paid, name="mark_order_paid"),
]
