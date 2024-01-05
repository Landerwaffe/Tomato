from django import forms
from Tomato import models

class CreateBooking(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = ['date','guests','preferences']