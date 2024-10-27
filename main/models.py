from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    restaurant = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=25)
    open_time = models.CharField(max_length=15)
    description = models.TextField()
    image = models.TextField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.its.ac.id%2Ftmesin%2Ffasilitas%2Flaboratorium-2%2Fno-image%2F&psig=AOvVaw3MxCmHHuz26CagUzVTBH79&ust=1729935269596000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMiWpJudqYkDFQAAAAAdAAAAABAJ')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
