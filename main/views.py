import datetime
import json
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
from bookmark.models import Bookmark
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

    food = Food.objects.all()

    if query:
        food = food.filter(name__icontains=query)

    if price_min:
        food = food.filter(price__gte=price_min)
    if price_max:
        food = food.filter(price__lte=price_max)

    if sort == 'price-asc':
        food = food.order_by('price')
    elif sort == 'price-desc':
        food = food.order_by('-price')

    return HttpResponse(serializers.serialize("json", food), content_type="application/json")

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
    bookmarks = Bookmark.objects.filter(user=request.user).select_related('food')
    # user = request.user
    context = {
        'bookmarks': bookmarks,
        'user': request.user,
    }
    return render(request, 'bookmarks.html', context)

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
@csrf_exempt
@require_POST
def bookmark_food(request, food_id):
    try:
        food = get_object_or_404(Food, id=food_id)
        bookmark, created = Bookmark.objects.get_or_create(
            user=request.user,
            food=food,
            defaults={'created_at': datetime.datetime.now()}
        )

        if created:
            return JsonResponse({
                'status': 'success',
                'message': 'Food bookmarked successfully',
                'is_bookmarked': True
            })
        else:
            # If bookmark already exists, remove it
            bookmark.delete()
            return JsonResponse({
                'status': 'success',
                'message': 'Bookmark removed successfully',
                'is_bookmarked': False
            })

    except Food.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Food not found'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

def bookmark_list(request, food_id):
    try:
        is_bookmarked = Bookmark.objects.filter(
            user=request.user,
            food_id=food_id
        ).exists()
        
        return JsonResponse({
            'status': 'success',
            'is_bookmarked': is_bookmarked
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

def bookmarks_view(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmarks.html', {'bookmarks': bookmarks})