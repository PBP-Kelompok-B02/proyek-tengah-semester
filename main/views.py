import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    context = {
        'group' : 'PBP B02',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

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

def show_detail(request, uuid):
    #get makanan by uuid soon

    #dummy data
    makanan = {
        "nama_makanan": "Nasi Goreng",
        "rating": 4.5,
        "deskripsi_makanan": "Nasi goreng dengan telur dan ayam",
        "harga": 20000,
        "lokasi": "Jakarta",
        "nama_tempat": "Warung Makan Pak Budi",
        "alamat": "Jl. Merdeka No. 10, Jakarta"
    }

    review_users = [
        {
            "name": "Hizounya",
            "review": "Great taste, will come back again!",
            #"img_path": "images/review1.jpg",
        },
        {
            "name": "Ara",
            "review": "Nice ambiance but the food was average.",
            # "img_path": None,
        },
        {
            "name": "Salsa",
            "review": "Loved the service and the food.",
            #"img_path": "images/review2.jpg",
        },
    ]

    context = {
        "makanan" : makanan,
        "review" : review_users
    }

    return render(request, "detail-makanan.html", context)
