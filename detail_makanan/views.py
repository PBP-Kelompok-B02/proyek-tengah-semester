from django.shortcuts import render,get_object_or_404
from .models import Food, FoodReviews

def show_food_details(request, name):
    food = get_object_or_404(Food, name=name)
    food_reviews = food.foodreviews_set.all()
    context = {
        'food': food,
        'reviews': food_reviews
    }
    return render(request, 'food_details.html', context)
