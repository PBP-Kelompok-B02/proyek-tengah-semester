from django.urls import path
from .views import show_food_details

app_name = 'detail_makanan'

urlpatterns = [
    path('<name>', show_food_details, name="food-details")
]