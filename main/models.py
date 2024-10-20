from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    restaurant = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    open_time = models.CharField(max_length=15)
    description = models.CharField(max_length=100)