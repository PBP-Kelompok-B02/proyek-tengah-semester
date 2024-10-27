from django.urls import path
from .views import show_forum, create_forum, submit_forum, delete_forum, reply_forum, delete_reply

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('create_forum/', create_forum, name='create_forum'),
    path('submit_forum/', submit_forum, name='submit_forum'),
    path('<int:forum_id>/delete/', delete_forum, name='delete_forum'),  
    path('<int:forum_id>/reply/', reply_forum, name='reply_forum'),  
    path('<int:reply_id>/delete-reply/', delete_reply, name='delete_reply'),
]