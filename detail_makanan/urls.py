from django.urls import path
from .views import show_food_details, delete_food_details
from django.conf import settings
from django.conf.urls.static import static

app_name = 'detail_makanan'

# urls.py
from django.urls import path
from .views import show_food_details, delete_food_details
from django.conf import settings
from django.conf.urls.static import static

app_name = 'detail_makanan'

urlpatterns = [
    path('<uuid:id>', show_food_details, name="show-food-details"),
    path('delete-review/<int:id>/', delete_food_details, name='delete_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)