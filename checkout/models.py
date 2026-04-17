from django.db import models
import datetime
from django.utils import timezone
from django import forms


# Create your models here.
class CheckOut(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    checkout_email = models.EmailField()
    mobile = models.CharField(max_length=15, default='')
    address = models.TextField()
    product_qty = models.FloatField()
    products_id = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    
    Payment_status = models.CharField(max_length=10, choices=(
        ('Paid', 'Paid'),
        ('Pending', 'Pending')
    ))
   
    Payment_type = models.CharField(max_length=20, choices=(
        ('COD', 'COD'),
        ('Online', 'Online')
    ))
    OrderPrice = models.CharField(max_length=20)
    checkout_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Order #{self.id}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-checkout_date']