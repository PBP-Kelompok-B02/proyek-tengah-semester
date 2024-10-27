from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            db_table = 'main_forum'  

    def __str__(self):
        return self.title
    
class Reply(models.Model):
    forum = models.ForeignKey(Forum, related_name='replies', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reply by {self.created_by.username} on {self.forum.title}'