from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm


# Create your views here.

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = BookingForm()  
     
    context = {
        "form": form,
    }    
    return render(request, 'booking.html', context)


def users(request):
    
    user_info = Booking.objects.all()

    context = {
        'user_info': user_info,
    }

    return render(request, 'booking.html', context)    
