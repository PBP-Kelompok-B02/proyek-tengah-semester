from django.urls import path
from .views import show_forum, create_forum, submit_forum, delete_forum, reply_forum, delete_reply, show_json, submit_forum_mobile, reply_forum_mobile, delete_forum_mobile, delete_reply_mobile

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('json/', show_json, name='show_json'), 
    path('create_forum/', create_forum, name='create_forum'),
    path('submit_forum/', submit_forum, name='submit_forum'),
    path('<int:forum_id>/delete/', delete_forum, name='delete_forum'),  
    path('<int:forum_id>/reply/', reply_forum, name='reply_forum'),  
    path('<int:reply_id>/delete-reply/', delete_reply, name='delete_reply'),
    path('submit-forum/mobile/', submit_forum_mobile, name='submit_forum_mobile'),  
    path('<int:forum_id>/reply/mobile/', reply_forum_mobile, name='reply_forum_mobile'),  
    path('<int:forum_id>/delete/mobile/', delete_forum_mobile, name='delete_forum_mobile'),
    path('<int:reply_id>/delete-reply/mobile/', delete_reply_mobile, name='delete_reply_mobile'),
]