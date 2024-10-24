from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Food
from .forms import FoodReviewForm

def show_food_details(request, name):
    food = get_object_or_404(Food, name=name)
    food_reviews = food.foodreviews_set.all()

    if request.method == 'POST':
        form = FoodReviewForm(request.POST, request.FILES)
        if form.is_valid():
            food_review = form.save(commit=False)
            food_review.user = request.user
            food_review.food = food
            food_review.save()

            return redirect(f'/food-details/{food.name}')
    else if request.method == 'DELETE':
        
    else:
        form = FoodReviewForm()

    context = {
        'food': food,
        'reviews': food_reviews,
        'form': form
    }
    
    return render(request, 'food-details.html', context)