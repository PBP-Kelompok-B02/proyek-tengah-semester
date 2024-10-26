from django.urls import path
from .views import show_main, show_json, register, login_user, logout_user, show_profile, show_bookmarks,show_forum, show_food_details, change_password, add_food_entry_ajax, get_user_foods_custom

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'), 
    path('profile/', show_profile, name='profile'),
    path('bookmark/', show_bookmarks, name='bookmark'),
    path('forum/', show_forum, name='forum'),
    path('food-details/<name>', show_food_details, name='food_details'), 
    path('change-password/', change_password, name='change_password'),
    path('create-food-entry-ajax', add_food_entry_ajax, name='add_food_entry_ajax'),
    path('get-user-foods/', get_user_foods_custom, name='get_user_foods'),
]