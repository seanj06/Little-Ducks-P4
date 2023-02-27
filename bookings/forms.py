from django.forms import ModelForm
from .models import Booking
from django import forms


class BookingForm(ModelForm):
    
    class Meta:
        model = Booking
        exclude = ['user', 'time_of_booking']



