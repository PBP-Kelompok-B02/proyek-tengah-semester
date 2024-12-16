from django.urls import include, path
from .views import show_main, show_json, register, login_user, logout_user, show_bookmarks,add_products_from_csv, bookmark_food, bookmark_list, bookmarks_view

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'), 
    path('forum/', include('forum.urls')), 
    path('bookmarks/', show_bookmarks, name='show_bookmarks'),
    path('add-products-from-csv/', add_products_from_csv, name='add_products_from_csv'),
    path('bookmark/<uuid:food_id>/', bookmark_food, name='bookmark_food'),
    path('bookmarks/<uuid:food_id>', bookmark_list, name='bookmark'),
    path('bookmarks/', bookmarks_view, name='bookmark_view'),
]