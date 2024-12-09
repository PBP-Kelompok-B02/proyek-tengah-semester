from django.urls import path
from .views import show_food_details, delete_food_details, show_food_details_json, delete_food_details_json
from django.conf import settings
from django.conf.urls.static import static

# urls.py

app_name = 'detail_makanan'

urlpatterns = [
    path('<uuid:id>', show_food_details, name="show-food-details"),
    path('delete-review/<int:id>/', delete_food_details, name='delete_review'),

    # json flutter
    path('json/<uuid:id>/', show_food_details_json, name="show-food-details-json"),
    path('json/delete-review/<int:id>', delete_food_details_json, name="delete-food-details-json"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)