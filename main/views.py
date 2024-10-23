import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers 
from .models import Food
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
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
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required
def show_profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)

@login_required
def show_bookmarks(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'bookmarks.html', context)

def show_forum(request):
    user = request.user
    context = {
        'user': user if user else None,
    }
    return render(request, 'forum.html', context)
