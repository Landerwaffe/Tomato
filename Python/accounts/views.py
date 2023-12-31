from django.shortcuts import render
from Tomato.models import Listing
from Tomato.models import Booking
from django.http import HttpResponse

def register(request):

        return render(request, 'register.html')
