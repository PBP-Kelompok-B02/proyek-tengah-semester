from django.urls import path
from .views import delete_forum, delete_reply, show_main, show_json, register, login_user, logout_user, show_profile, show_bookmarks, show_forum, show_food_details, create_forum, submit_forum, reply_forum

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'), 
    path('profile/', show_profile, name='profile'),
    path('bookmark/', show_bookmarks, name='bookmark'),
    path('food-details/<name>', show_food_details, name='food_details'), 
    
    path('forum/<int:forum_id>/delete/', delete_forum, name='delete_forum'),
    path('reply/<int:reply_id>/delete/', delete_reply, name='delete_reply'), 

    path('forum/', show_forum, name='forum'),
    path('forum/create_forum/', create_forum, name='create_forum'),
    path('forum/submit_forum/', submit_forum, name='submit_forum'),
    path('forum/<int:forum_id>/delete/', delete_forum, name='delete_forum'),
    path('forum/<int:forum_id>/reply/', reply_forum, name='reply_forum'),
]