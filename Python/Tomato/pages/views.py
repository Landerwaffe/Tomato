from django.shortcuts import render, redirect
from Tomato.models import Listing, Booking, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Tomato import forms

def home(request):
        profiles = Profile.objects.filter(user = request.user.id)
        context = {'profiles': profiles}
        return render(request, 'home.html', context)

def listings(request):
        listings = Listing.objects.all()
        bookings = Booking.objects.all().order_by('date')
        return render(request, 'listings.html', {'listings': listings})

def contact(request):

        return render(request, 'contact.html')

def about(request):

        return render(request, 'about.html')

def listing_detail(request, slug, id):
        listings = Listing.objects.get(pk = id)
        return render(request, 'listing_detail.html', {'listings' : listings})

@login_required(login_url = "/login/")
def profile(request):

        user = User.objects.get(pk = request.user.id)

        if request.method == 'POST':
                form = forms.EditFirstName(request.POST, instance = user) 
        # request.FILES if submitting files
                if form.is_valid():
                   form.save()
                   return redirect('/profile/')
        else:
             form = forms.EditFirstName()
        
        profiles = Profile.objects.filter(user = request.user.id)
        context = {'profiles': profiles, 'form': form}
        return render(request, 'profile.html', context)

def edit(request):
       
        user = User.objects.get(pk = request.user.id)

        if request.method == 'POST':
                form = forms.EditFirstName(request.POST, instance = user) 
        # request.FILES if submitting files
                if form.is_valid():
                   form.save()
                   return redirect('/profile/')
        else:
             form = forms.EditFirstName()
        
        profiles = Profile.objects.filter(user = request.user.id)
        context = {'profiles': profiles, 'form': form}
        return render(request, 'edit.html', context)
