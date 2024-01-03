from django import forms
from Tomato import models

class CreateBooking(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = ['listing','date','guests','preferences']

class EditFirstName(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['first_name']
