from django.urls import path
from .views import show_profile, change_password, add_food_entry_ajax, edit_food_ajax, delete_food_ajax, get_food_detail, get_user_foods, create_food_flutter, show_json, edit_food_flutter, change_password_flutter

app_name = 'dashboard'

urlpatterns = [
    path('', show_profile, name='profile'),
    path('change-password/', change_password, name='change_password'),
    path('add-food/', add_food_entry_ajax, name='add_food'),
    path('edit-food/<uuid:id>/', edit_food_ajax, name='edit_food'),
    path('delete-food/<uuid:id>/', delete_food_ajax, name='delete_food'),
    path('get-food/<uuid:id>/', get_food_detail, name='get_food'),
    path('get-user-foods/', get_user_foods, name='get_user_foods'),
    path('create-flutter/', create_food_flutter, name='create_food_flutter'),
    path('json/', show_json, name='show_json'),
    path('edit-flutter/<uuid:id>/', edit_food_flutter, name='edit_food_flutter'),
    path('change-password-flutter/', change_password_flutter, name='change_password_flutter')
]