from django import forms
from .models import FoodReviews

class FoodReviewForm(forms.ModelForm):
    class Meta:
        model = FoodReviews
        fields = ['review', 'image_url']
        widgets = {
            'image_url': forms.FileInput()
        }
