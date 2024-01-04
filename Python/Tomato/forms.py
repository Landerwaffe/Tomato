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

class EditLastName(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['last_name']

class EditEmail(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['email']

class EditGender(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['gender']

class EditPassword(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['password']

class EditPicture(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['picture']