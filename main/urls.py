from django.urls import path
from .views import show_main, show_json, register, login_user, logout_user, show_profile, show_bookmarks,show_forum, change_password, add_food_entry_ajax, edit_food_ajax, delete_food_ajax, get_food_detail, get_user_foods, create_forum, submit_forum, delete_forum, reply_forum, delete_reply,add_products_from_csv, bookmark_food, bookmark_list, bookmarks_view

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'), 
    path('profile/', show_profile, name='profile'),
    path('bookmarks/', show_bookmarks, name='show_bookmarks'),
    path('forum/', show_forum, name='forum'),
    path('forum/create_forum/', create_forum, name='create_forum'),
    path('forum/submit_forum/', submit_forum, name='submit_forum'),
    path('forum/<int:forum_id>/delete/', delete_forum, name='delete_forum'),  
    path('forum/<int:forum_id>/reply/', reply_forum, name='reply_forum'),  # URL baru untuk menambah reply
    path('forum/<int:reply_id>/delete-reply/', delete_reply, name='delete_reply'),
    path('add-products-from-csv/', add_products_from_csv, name='add_products_from_csv'),
    path('change-password/', change_password, name='change_password'),
    path('add-food/', add_food_entry_ajax, name='add_food'),
    path('edit-food/<uuid:food_id>/', edit_food_ajax, name='edit_food'),
    path('delete-food/<uuid:food_id>/', delete_food_ajax, name='delete_food'),
    path('get-food/<uuid:food_id>/', get_food_detail, name='get_food'),
    path('get-user-foods/', get_user_foods, name='get_user_foods'),
    path('bookmark/<uuid:food_id>/', bookmark_food, name='bookmark_food'),
    path('bookmarks/<uuid:food_id>', bookmark_list, name='bookmark'),
    path('bookmarks/', bookmarks_view, name='bookmark_view'),
]