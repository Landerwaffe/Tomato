from django.shortcuts import render, redirect
from Tomato.models import Listing, Booking, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Tomato import forms
from django.contrib.auth.forms import PasswordChangeForm

def home(request):
        profiles = Profile.objects.filter(user = request.user.id)
        context = {'profiles': profiles}
        return render(request, 'index.html', context)

def listings(request):
        listings = Listing.objects.all()
        profiles = Profile.objects.filter(user = request.user.id)
        # bookings = Booking.objects.all().order_by('date')
        context = {'profiles': profiles, 'listings': listings}
        return render(request, 'listings.html', context)

def query(request):
        profiles = Profile.objects.filter(user = request.user.id)
        print(request.GET)
        min = -1
        max = -1
        query_dict = request.GET # this is a dictionary
        query = query_dict.get("query")
        if "-" in query:
              print("- found!")
              list = query.split('-')
              print(list[0])
              print(list[1])
              min = list[0]
              max = list[1]
        listings = Listing.objects.filter(title__icontains = query)
        countrysearch = Listing.objects.filter(country__icontains = query)
        pricesearch = Listing.objects.filter(pricepernight__range=(min, max))
        amenitysearch = Listing.objects.filter(amenities__icontains = query)
        shortdescriptionsearch = Listing.objects.filter(shortdescription__icontains = query)
        longdescriptionsearch = Listing.objects.filter(longdescription__icontains = query)
        # print("Country search returns:")
        # print(countrysearch)
        context = {'profiles': profiles, 'listings': listings, 'countrysearch': countrysearch, 'pricesearch': pricesearch , 'amenitysearch': amenitysearch, 'shortdescriptionsearch': shortdescriptionsearch, 'longdescriptionsearch': longdescriptionsearch}
        return render(request, 'query.html', context)

def contact(request):
        profiles = Profile.objects.filter(user = request.user.id)
        context = {'profiles': profiles}
        return render(request, 'contact.html', context)

def about(request):
        profiles = Profile.objects.filter(user = request.user.id)
        context = {'profiles': profiles}
        return render(request, 'about.html', context)

def listing_detail(request, slug, id):
        listings = Listing.objects.get(pk = id)
        profiles = Profile.objects.filter(user = request.user.id)
        context = {'profiles': profiles, 'listings': listings}
        return render(request, 'listing_detail.html', context)

@login_required(login_url = "/login/")
def profile(request):  
        profiles = Profile.objects.filter(user = request.user.id)
        context = {'profiles': profiles}
        return render(request, 'profile.html', context)

def editfirstname(request):
       
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
        return render(request, 'editfirstname.html', context)

def editlastname(request):
       
        user = User.objects.get(pk = request.user.id)

        if request.method == 'POST':
                form = forms.EditLastName(request.POST, instance = user) 
        # request.FILES if submitting files
                if form.is_valid():
                   form.save()
                   return redirect('/profile/')
        else:
             form = forms.EditLastName()
        
        profiles = Profile.objects.filter(user = request.user.id)
        context = {'profiles': profiles, 'form': form}
        return render(request, 'editlastname.html', context)

def editemail(request):
       
        user = User.objects.get(pk = request.user.id)

        if request.method == 'POST':
                form = forms.EditEmail(request.POST, instance = user) 
        # request.FILES if submitting files
                if form.is_valid():
                   form.save()
                   return redirect('/profile/')
        else:
             form = forms.EditEmail()
        
        profiles = Profile.objects.filter(user = request.user.id)
        context = {'profiles': profiles, 'form': form}
        return render(request, 'editemail.html', context)

def editgender(request):
       
        # user = User.objects.get(pk = request.user.id)
        profile = Profile.objects.get(user = request.user.id)
        profiles = Profile.objects.filter(user = request.user.id)

        if request.method == 'POST':
                form = forms.EditGender(request.POST, instance = profile) 
        # request.FILES if submitting files
                if form.is_valid():
                   form.save()
                   return redirect('/profile/')
        else:
             form = forms.EditGender()
        
        context = {'profiles': profiles, 'form': form, 'profile': profile}
        return render(request, 'editgender.html', context)

def editpassword(request):
       
        if request.method == 'POST':
                form = PasswordChangeForm(user = request.user, data = request.POST) 
        # request.FILES if submitting files
                if form.is_valid():
                   form.save()
                   return redirect('/profile/')
        else:
             form = PasswordChangeForm(user = request.user)
        
        profiles = Profile.objects.filter(user = request.user.id)
        context = {'profiles': profiles, 'form': form}
        return render(request, 'editpassword.html', context)

def editpicture(request):
       
        # user = User.objects.get(pk = request.user.id)
        profile = Profile.objects.get(user = request.user.id)
        profiles = Profile.objects.filter(user = request.user.id)

        if request.method == 'POST':
                form = forms.EditPicture(request.POST, request.FILES, instance = profile) 
        # request.FILES if submitting files
                if form.is_valid():
                   form.save()
                   return redirect('/profile/')
        else:
             form = forms.EditPicture()
        
        context = {'profiles': profiles, 'form': form, 'profile': profile}
        return render(request, 'editpicture.html', context)