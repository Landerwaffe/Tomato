from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Tomato.models import Listing
from Tomato.models import Booking
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms

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
                if 'next' in request.POST:
                     return redirect(request.POST.get('next'))
                else:
                    return redirect("/listings/")
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def signout(request):
     if request.method == 'POST':
        logout(request)
        return redirect("/listings/")
         
@login_required(login_url = "/login/")
def booking(request):
     if request.method == 'POST':
        form = forms.CreateBooking(request.POST) 
        # request.FILES if submitting files
        if form.is_valid():
             instance = form.save(commit=False)
             instance.author = request.user
             instance.save()
             return redirect('/listings/')
     else:
        form = forms.CreateBooking()
     return render(request, 'booking.html', {'form': form})

@login_required(login_url = "/login/")
def history(request):
     bookings = Booking.objects.filter(author = request.user.id)
     return render(request, 'history.html', {'bookings': bookings})