from django.urls import include, path
from .views import show_main, show_json, register, login_user, logout_user, show_profile, show_bookmarks, change_password, add_food_entry_ajax, edit_food_ajax, delete_food_ajax, get_food_detail, get_user_foods,add_products_from_csv, bookmark_food, bookmark_list, bookmarks_view

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'), 
    path('profile/', show_profile, name='profile'),
    path('forum/', include('forum.urls')), 
    path('bookmarks/', show_bookmarks, name='show_bookmarks'),
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