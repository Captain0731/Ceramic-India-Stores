from django.db import models

# Create your models here.

class Estimate(models.Model):
    apartment_type = models.CharField(max_length=10,choices=(
        ('1000',"1000"),
        ('2000',"2000"),
        ('3000',"3000"),
        ('4000',"4000"),
        ('50000',"5000"),
        ('6000',"6000"),
        ('7000',"7000"),
        ('8000',"8000"),
        ('9000',"9000"),
        ('10000',"10000")

    ))

    bedroomes_type = models.CharField(max_length=50,choices=(
        ('1',"1"),
        ('2',"2"),
        ('3',"3"),
        ('4',"4"),
        ('5',"5")
    ))

    modular_kitchen = models.CharField(max_length=10)

    Carpet_area_in_sqft = models.CharField(max_length=10)