from django.db import models
from django.contrib.auth.models import User
import uuid

class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    restaurant = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    open_time = models.CharField(max_length=15)
    description = models.TextField()
    image = models.TextField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.its.ac.id%2Ftmesin%2Ffasilitas%2Flaboratorium-2%2Fno-image%2F&psig=AOvVaw3MxCmHHuz26CagUzVTBH79&ust=1729935269596000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMiWpJudqYkDFQAAAAAdAAAAABAJ')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# class Forum(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#             db_table = 'main_forum'  # Ex

#     def __str__(self):
#         return self.title
    
# class Reply(models.Model):
#     forum = models.ForeignKey(Forum, related_name='replies', on_delete=models.CASCADE)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Reply by {self.created_by.username} on {self.forum.title}'