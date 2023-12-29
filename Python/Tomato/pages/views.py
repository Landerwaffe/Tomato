from django.shortcuts import render
from Tomato.models import Listing
from Tomato.models import Booking

def home(request):

        return render(request, 'home.html')

def listings(request):
        listings = Listing.objects.all()
        bookings = Booking.objects.all().order_by('date')
        return render(request, 'listings.html', {'listings': listings})

def contact(request):

        return render(request, 'contact.html')

def about(request):

        return render(request, 'about.html')