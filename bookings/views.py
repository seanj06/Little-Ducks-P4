from django.shortcuts import render
from .models import Booking


# Create your views here.
def booking(request):
    
    booking_info = Booking.objects.all()

    context = {
        'booking_info': booking_info
    }

    return render(request, 'booking.html', context)


