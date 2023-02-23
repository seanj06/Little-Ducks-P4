from django.shortcuts import render
from .models import Booking
from .forms import BookingForm


# Create your views here.

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.Post) 
    else:
        form = BookingForm()    

    context = {
        "form": form,
    }    
    return render(request, 'booking.html', context)
