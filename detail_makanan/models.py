import uuid
from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    restaurant = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    open_time = models.CharField(max_length=15)
    description = models.CharField(max_length=100)

class FoodReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    review = models.CharField(max_length=500)
    image_url = models.ImageField(upload_to='review_images/', blank=True, null=True)