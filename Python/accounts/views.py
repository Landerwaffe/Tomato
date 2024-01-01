from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Tomato.models import Listing
from Tomato.models import Booking
from django.http import HttpResponse
from django.contrib.auth import login, logout

def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  user = form.save()
                  #log the user in
                  login(request, user)
                  return redirect("/listings/")
        else:
            form = UserCreationForm()      
        return render(request, 'register.html', {'form': form})

def signin(request):
        if request.method == 'POST':
            form = AuthenticationForm(data = request.POST)
            if form.is_valid():
                # log in the user
                user = form.get_user()
                login(request, user)
                return redirect("/listings/")
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def signout(request):
     if request.method == 'POST':
        logout(request)
        return redirect("/listings/")
         