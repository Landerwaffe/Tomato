from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Tomato.models import Booking, Profile, Listing
from django.contrib.auth.models import User
from accounts.forms import CreateProfile
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms

def register(request):
        profiles = Profile.objects.filter(user = request.user.id)
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            profileform = CreateProfile(request.POST, request.FILES)
            if form.is_valid() and profileform.is_valid():
                  user = form.save()
                  instance = profileform.save(commit=False)
                  registereduser = User.objects.latest('id')
                  instance.user = registereduser
                  instance.save()
                  #log the user in
                  login(request, user)
                  return redirect("/listings/")
        else:
            form = UserCreationForm()   
            profileform = CreateProfile()

        context = {'profiles': profiles, 'form': form, 'profileform': profileform}
        return render(request, 'register.html', context)

def signin(request):
        profiles = Profile.objects.filter(user = request.user.id)
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
        
        context = {'profiles': profiles, 'form': form}
        return render(request, 'login.html', context)

def signout(request):
     if request.method == 'POST':
        logout(request)
        return redirect("/listings/")
         
@login_required(login_url = "/login/")
def booking(request, slug, id):
     # print(request.get_full_path()) //Note for future

     profiles = Profile.objects.filter(user = request.user.id)
     listings = Listing.objects.get(pk = id)
     if request.method == 'POST':
        form = forms.CreateBooking(request.POST) 
        # request.FILES if submitting files
        if form.is_valid():
             instance = form.save(commit=False)
             instance.author = request.user
             instance.listing = listings
             instance.save()
             return redirect('/listings/')
     else:
        form = forms.CreateBooking()
     context = {'profiles': profiles, 'form': form, 'listings': listings}
     return render(request, 'booking.html', context)

@login_required(login_url = "/login/")
def history(request):
     profiles = Profile.objects.filter(user = request.user.id)
     bookings = Booking.objects.filter(author = request.user.id)
     context = {'profiles': profiles, 'bookings': bookings}
     return render(request, 'history.html', context)