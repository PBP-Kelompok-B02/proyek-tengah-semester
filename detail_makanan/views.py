# views.py
import os
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodReviews
from main.models import Food
from .forms import FoodReviewForm

def show_food_details(request,id):
    food = get_object_or_404(Food, pk=id)
    if not food:
        return JsonResponse({'error': 'Food not found.'}, status=404)
    food_reviews = food.foodreviews_set.all().order_by('-id')

    if request.method == 'POST':
        form = FoodReviewForm(request.POST, request.FILES)
        if form.is_valid():
            food_review = form.save(commit=False)
            food_review.user = request.user
            food_review.food = food
            food_review.save()

            return redirect(f'/food-details/{food.pk}')
    else:
        form = FoodReviewForm()

    context = {
        'food': food,
        'reviews': food_reviews,
        'form': form
    }
    
    return render(request, 'food-details.html', context)

def delete_food_details(request, id):
    if request.method == 'POST':
        try:
            food_review = get_object_or_404(FoodReviews, id=id, user=request.user)

            image_path = food_review.image_url.path if food_review.image_url else None

            food_review.delete()

            if image_path and os.path.exists(image_path):
                os.remove(image_path)

            return redirect(f'/food-details/{food_review.food.pk}')
        except FoodReviews.DoesNotExist:
            return JsonResponse({'error': 'Review not found or not authorized.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)