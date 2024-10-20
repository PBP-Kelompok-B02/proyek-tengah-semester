from django.urls import path
from main.views import show_main, show_detail,register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('detail-makanan/<int:uuid>', show_detail, name="show_detail")
]