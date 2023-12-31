from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Tomato.models import Listing
from Tomato.models import Booking
from django.http import HttpResponse

def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  form.save()
                  #log the user in
                  return redirect("/listings/")
        else:
            form = UserCreationForm()      
        return render(request, 'register.html', {'form': form})

def login(request):
        if request.method == 'POST':
            form = AuthenticationForm(data = request.POST)
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})