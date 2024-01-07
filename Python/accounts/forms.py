from django import forms
from Tomato import models

class CreateBooking(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = ['date','guests','preferences']

class CreateProfile(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['picture', 'gender']