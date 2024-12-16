import json
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Food
from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.utils.html import strip_tags
from django.core import serializers

@login_required
def show_profile(request):
    if request.user.is_authenticated:
        user_foods = Food.objects.filter(user=request.user)  
        context = { 'user_foods': user_foods }
        return render(request, 'profile.html', context)
    else:
        return redirect('main:login') 
    
@csrf_exempt
@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)

        user = request.user
        if not user.check_password(old_password):
            return JsonResponse({'error': 'Old password is incorrect'}, status=400)

        user.set_password(new_password)
        user.save()

        update_session_auth_hash(request, user)

        return JsonResponse({'success': 'Password changed successfully'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def get_user_foods(request):
    try:
        user_foods = Food.objects.filter(user=request.user) 
        foods_data = []
        
        for food in user_foods:
            foods_data.append({
                'id': food.id,
                'name': food.name,
                'price': food.price,
                'restaurant': food.restaurant,
                'address': food.address,
                'contact': food.contact,
                'open_time': food.open_time,
                'description': food.description,
                'image': food.image
            })

        return JsonResponse({
            'status': 'success',
            'foods': foods_data
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

@csrf_exempt
@require_POST
def add_food_entry_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status': 'error', 'message': 'User not authenticated'}, status=401)
    
    try:
        new_food = Food(
            user=request.user, 
            name=strip_tags(request.POST.get('name')),
            price=request.POST.get('price'),
            restaurant=strip_tags(request.POST.get('restaurant')),
            address=strip_tags(request.POST.get('address')),
            contact=strip_tags(request.POST.get('contact')),
            open_time=strip_tags(request.POST.get('open_time')),
            description=strip_tags(request.POST.get('description')),
            image=strip_tags(request.POST.get('image'))
        )
        
        if 'image' in request.FILES:
            new_food.image = request.FILES['image']
            
        new_food.save()
        return JsonResponse({'status': 'success'})
        
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@login_required
@require_POST
def edit_food_ajax(request, id):
    try:
        food = Food.objects.get(pk=id, user=request.user)

        food.name = strip_tags(request.POST.get('name', food.name))
        food.price = request.POST.get('price', food.price)
        food.restaurant = strip_tags(request.POST.get('restaurant', food.restaurant))
        food.address = strip_tags(request.POST.get('address', food.address))
        food.contact = strip_tags(request.POST.get('contact', food.contact))
        food.open_time = strip_tags(request.POST.get('open_time', food.open_time))
        food.description = strip_tags(request.POST.get('description', food.description))
        food.image = strip_tags(request.POST.get('image', food.image))
        
        food.save()
        return JsonResponse({'status': 'success'})
        
    except Food.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Food not found or access denied'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@login_required
@require_POST
def delete_food_ajax(request, id):
    try:
        print(f"Attempting to delete food with ID: {id}")
        food = get_object_or_404(Food, pk=id, user=request.user)
        food.delete()
        print(f"Successfully deleted food with ID: {id}")
        return JsonResponse({'status': 'success'})
    except Food.DoesNotExist:
        print(f"Food with ID: {id} not found or access denied")
        return JsonResponse({'status': 'error', 'message': 'Food not found or access denied'}, status=404)
    except Exception as e:
        print(f"Error deleting food with ID: {id} - {str(e)}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@login_required
def get_food_detail(request, id):
    try:
        food = get_object_or_404(Food, pk=id, user=request.user)
        return JsonResponse({
            'status': 'success',
            'food': {
                'id': food.id,
                'name': food.name,
                'price': food.price,
                'restaurant': food.restaurant,
                'address': food.address,
                'contact': food.contact,
                'open_time': food.open_time,
                'description': food.description,
                'image': food.image
            }
        })
    except Food.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Food not found or access denied'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
@csrf_exempt
def create_food_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_food = Food.objects.create(
            user=request.user, 
            name=data["name"],
            price=int(data["price"]),
            restaurant=data["restaurant"],
            address=data["address"],    
            contact=data["contact"],
            open_time=data["open_time"],
            description=data["description"],
            image=data["image"]
        )

        new_food.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt  
def show_json(request):
    data = Food.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def edit_food_flutter(request, id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            food = Food.objects.get(id=id, user=request.user)
            
            food.name = data.get("name", food.name)
            food.price = int(data.get("price", food.price))
            food.restaurant = data.get("restaurant", food.restaurant)
            food.address = data.get("address", food.address)
            food.contact = data.get("contact", food.contact)
            food.open_time = data.get("open_time", food.open_time)
            food.description = data.get("description", food.description)
            food.image = data.get("image", food.image)
            food.save()
            
            return JsonResponse({'status': 'success', 'message': 'Food updated successfully'})
        except Food.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Food not found or access denied'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
    
@csrf_exempt
@login_required
def change_password_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            old_password = data.get('old_password')
            new_password = data.get('new_password')
            confirm_password = data.get('confirm_password')

            if new_password != confirm_password:
                return JsonResponse({'status': 'error', 'message': 'Passwords do not match'}, status=400)

            user = request.user
            if not user.check_password(old_password):
                return JsonResponse({'status': 'error', 'message': 'Old password is incorrect'}, status=400)

            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Penting untuk memperbarui hash autentikasi sesi

            return JsonResponse({'status': 'success', 'message': 'Password changed successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
    
@csrf_exempt
@login_required
def delete_food_flutter(request, id):
    try:
        print(f"Attempting to delete food with ID: {id}")
        food = get_object_or_404(Food, pk=id, user=request.user)
        food.delete()
        print(f"Successfully deleted food with ID: {id}")
        return JsonResponse({'status': 'success'})
    except Food.DoesNotExist:
        print(f"Food with ID: {id} not found or access denied")
        return JsonResponse({'status': 'error', 'message': 'Food not found or access denied'}, status=404)
    except Exception as e:
        print(f"Error deleting food with ID: {id} - {str(e)}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)