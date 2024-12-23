# views.py
import os, logging, json, base64
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from .models import FoodReviews
from main.models import Food
from .forms import FoodReviewForm
from django.views.decorators.csrf import csrf_exempt
logger = logging.getLogger(__name__)

def show_food_details(request,id):
    logger.info("Received request for show_food_details")
    food = get_object_or_404(Food, pk=id)
    if not food:
        return JsonResponse({'error': 'Food not found.'}, status=404)
    food_reviews = food.foodreviews_set.all().order_by('-id')

    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = FoodReviewForm(request.POST, request.FILES)
        if form.is_valid():
            food_review = form.save(commit=False)
            food_review.user = request.user
            food_review.food = food
            food_review.save()

            reviews_html = render_to_string('review.html', {'reviews': food_reviews, 'request': request})
            return JsonResponse({'success': True, 'html': reviews_html})

        return JsonResponse({'success': False, 'error': form.errors.as_json()}, status=400)

    elif request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        reviews_html = render_to_string('review.html', {'reviews': food_reviews, 'request': request})
        return JsonResponse({'success': True, 'html': reviews_html})

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

            return JsonResponse({'success': True, 'message': 'Review deleted successfully'})
        except FoodReviews.DoesNotExist:
            return JsonResponse({'error': 'Review not found or not authorized.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)

@csrf_exempt
def show_food_details_json(request, id):
    food = get_object_or_404(Food, pk=id)
    food_reviews = food.foodreviews_set.all().order_by('-id')

    if request.method == 'POST':
        try:
            if request.content_type and 'application/json' in request.content_type:
                data = json.loads(request.body)
            else:
                data = request.POST.dict()

            review_text = data['review']
            base64_image = data['image'] if 'image' in data else "no image"

            food_review = FoodReviews(
                food=food,
                user=request.user,
                review=review_text
            )

            if base64_image != "no image":
                try:
                    # Remove potential data URL prefix
                    if ',' in base64_image:
                        base64_image = base64_image.split(',')[1]
                    image_flutter = ContentFile(base64.b64decode(base64_image), name=f"{food.name}_review.jpg")
                    food_review.image_url = image_flutter
                except Exception as e:
                    return JsonResponse({'success': False, 'error': 'Invalid image data'}, status=400)

            food_review.save()

            new_review = {
                'id': food_review.id,
                'user': food_review.user.username if food_review.user else 'Anonymous',
                'review': food_review.review,
                'image_url': food_review.image_url.url if food_review.image_url else None,
            }

            return JsonResponse({'success': True, 'new_review': new_review}, status=201)
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {str(e)}")
            return JsonResponse({'success': False, 'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return JsonResponse({'success': False, 'error': str(e)}, status=400)

    elif request.method == 'GET':
        food_data = {
            'id': str(food.id),
            'name': food.name,
            'price': float(food.price),
            'restaurant': food.restaurant,
            'address': food.address,
            'contact': food.contact,
            'open_time': food.open_time,
            'description': food.description,
            'image': food.image,
        }

        reviews_data = [
            {
                'id': review.id,
                'user': review.user.username if review.user else 'Anonymous',
                'review': review.review,
                'image_url': review.image_url.url if review.image_url else None,
            }
            for review in food_reviews
        ]

        response_data = {
            'food': food_data,
            'reviews': reviews_data,
        }

        return JsonResponse(response_data, safe=False)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@csrf_exempt
def delete_food_details_json(request, id):
    if request.method == 'POST':
        try:
            food_review = get_object_or_404(FoodReviews, id=id, user=request.user)

            image_path = food_review.image_url.path if food_review.image_url else None

            food_review.delete()

            if image_path and os.path.exists(image_path):
                os.remove(image_path)

            return JsonResponse({'success': True, 'message': 'Review deleted successfully'})
        except FoodReviews.DoesNotExist:
            return JsonResponse({'error': 'Review not found or not authorized.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)