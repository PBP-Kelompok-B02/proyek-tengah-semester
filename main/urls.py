from django.urls import path
from main.views import show_main
from main.views import show_detail

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('detail-makanan/<int:id>', show_detail, name="show_detail")
]