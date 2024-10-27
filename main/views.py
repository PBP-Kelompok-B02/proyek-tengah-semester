import datetime
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers 
from .models import Food
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash
from .forms import CSVUploadForm
from .models import Food
from forum.models import Forum, Reply
import csv
from django.shortcuts import render

import os
from django.conf import settings
from pathlib import Path

def show_main(request):
    context = {
        'is_authenticated': request.user.is_authenticated,
        'user': request.user,
    }
    return render(request, 'main.html', context)

def show_json(request):
    query = request.GET.get('query', '')
    sort = request.GET.get('sort', 'name')
    price_min = request.GET.get('price_min', '')
    price_max = request.GET.get('price_max', '')
    rating_min = request.GET.get('rating_min', '')
    rating_max = request.GET.get('rating_max', '')
    open_time_min = request.GET.get('open_time_min', '')
    open_time_max = request.GET.get('open_time_max', '')

    food = Food.objects.all()

    if query:
        food = food.filter(name__icontains=query)

    if price_min:
        food = food.filter(price__gte=price_min)
    if price_max:
        food = food.filter(price__lte=price_max)

    if rating_min:
        food = food.filter(rating__gte=rating_min)
    if rating_max:
        food = food.filter(rating__lte=rating_max)

    if open_time_min:
        food = food.filter(open_time__lte=open_time_min)
    if open_time_max:
        food = food.filter(open_time__gte=open_time_max)

    if sort == 'price-asc':
        food = food.order_by('price')
    elif sort == 'price-desc':
        food = food.order_by('-price')
    elif sort == 'rating-asc':
        food = food.order_by('rating')
    elif sort == 'rating-desc':
        food = food.order_by('-rating')

    return HttpResponse(serializers.serialize("json", food), content_type="application/json")

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

        # Update the session to keep the user logged in after the password change
        update_session_auth_hash(request, user)

        return JsonResponse({'success': 'Password changed successfully'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def register(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.delete_cookie('last_login')
    return response

@login_required
def show_profile(request):
    if request.user.is_authenticated:
        user_foods = Food.objects.filter(user=request.user)  
        context = { 'user_foods': user_foods }
        return render(request, 'profile.html', context)
    else:
        return redirect('login') 

@login_required
def show_bookmarks(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'bookmarks.html', context)

# def show_forum(request):
#     user = request.user
#     forums = Forum.objects.all().order_by('-created_at')

#     context = {
#         'user': user,
#         'forums': forums,
#     }
#     return render(request, 'forum.html', context)



# @login_required
# def create_forum(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')

#         # Buat topik diskusi baru dan assign created_by dengan request.user
#         Forum.objects.create(
#             title=title,
#             description=description,
#             created_by=request.user  # Tambahkan user sebagai pembuat
#         )

#         # Redirect setelah forum berhasil dibuat
#         return redirect('main:forum')
#     return render(request, 'create_forum.html')

# def submit_forum(request):
#     if request.method == 'POST':
#         # Handle form submission here
#         # For example, save the form data to the database
#         title = request.POST.get('title')
#         description = request.POST.get('description')

#         if title and description:
#             new_forum = Forum.objects.create(
#                 title=title,
#                 description=description,
#                 created_by=request.user  # Menggunakan user yang sudah login
#             )
#             return JsonResponse({'success': True})
#         else:
#             return JsonResponse({'success': False, 'message': 'Invalid data'})
    
#     return JsonResponse({'success': False, 'message': 'Invalid request'})

# @login_required
# @require_POST
# def delete_forum(request, forum_id):
#     forum = get_object_or_404(Forum, id=forum_id, created_by=request.user)
#     forum.delete()
#     return JsonResponse({'success': True})

# @login_required
# @require_POST
# def reply_forum(request, forum_id):
#     forum = get_object_or_404(Forum, id=forum_id)
#     content = request.POST.get('content')
    
#     if content:
#         reply = Reply.objects.create(
#             forum=forum,
#             created_by=request.user,
#             content=content
#         )
        
#         return JsonResponse({
#             'success': True,
#             'reply': {
#                 'id': reply.id,
#                 'content': reply.content,
#                 'username': reply.created_by.username,
#             }
#         })
#     return JsonResponse({'success': False, 'error': 'Content is required'}, status=400)


# @login_required
# @require_POST
# def delete_reply(request, reply_id):
#     reply = get_object_or_404(Reply, id=reply_id, created_by=request.user)
#     reply.delete()
#     return JsonResponse({'success': True})


def add_products_from_csv(request):
    user_now = request.user
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)

            for row in reader:
                try:
                    Food.objects.create(
                        name=row[0],
                        price=row[1],
                        restaurant=row[2],
                        address=row[3],
                        contact=row[4],
                        open_time=row[5],
                        description=row[6],
                        image=row[7],
                        user=user_now
                    )
                except IndexError:
                    messages.error(request, f"Error processing row: {row}")
                    continue

            messages.success(request, "Products added successfully!")
            return redirect('add_products_from_csv')
    else:
        form = CSVUploadForm()

    return render(request, 'add_products_from_csv.html', {'form': form})

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
            user=request.user,  # Assign the current user
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            restaurant=request.POST.get('restaurant'),
            address=request.POST.get('address'),
            contact=request.POST.get('contact'),
            open_time=request.POST.get('open_time'),
            description=request.POST.get('description'),
            image=request.POST.get('image')
        )
        
        if 'image' in request.FILES:
            new_food.image = request.FILES['image']
            
        new_food.save()
        return JsonResponse({'status': 'success'})
        
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@login_required
@require_POST
def edit_food_ajax(request, food_id):
    try:
        # Get food object that belongs to current user
        food = get_object_or_404(Food, user=request.user)
        
        # Update fields
        food.name = request.POST.get('name', food.name)
        food.price = request.POST.get('price', food.price)
        food.restaurant = request.POST.get('restaurant', food.restaurant)
        food.address = request.POST.get('address', food.address)
        food.contact = request.POST.get('contact', food.contact)
        food.open_time = request.POST.get('open_time', food.open_time)
        food.description = request.POST.get('description', food.description)
        
        if 'image' in request.FILES:
            food.image = request.FILES['image']
            
        food.save()
        return JsonResponse({'status': 'success'})
        
    except Food.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Food not found or access denied'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@login_required
@require_POST
def delete_food_ajax(request, food_id):
    try:
        # Get and delete food object that belongs to current user
        food = get_object_or_404(Food, pk=food_id, user=request.user)
        food.delete()
        return JsonResponse({'status': 'success'})
        
    except Food.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Food not found or access denied'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@login_required
def get_food_detail(request, food_id):
    try:
        # Get food object that belongs to current user
        food = get_object_or_404(Food, pk=food_id, user=request.user)
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
                'image': food.image.url if food.image else None
            }
        })
    except Food.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Food not found or access denied'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)