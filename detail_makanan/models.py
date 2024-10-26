import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from main.models import Food

# buat upload foodreview
def upload_to(instance, filename):
    current_time = now().strftime('%Y%m%d%H%M%S')
    return os.path.join('detail_makanan', 'reviews', f'{instance.food.name}', f'{current_time}_{filename}')

class FoodReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    review = models.CharField(max_length=500)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)


