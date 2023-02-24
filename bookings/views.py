from django.shortcuts import render, redirect, get_object_or_404
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


def booking_detail(request, id):
    booking = get_object_or_404(Booking, pk=id)

    context = {
        "booking": booking,
    }

    return render(request, 'booking-conf.html', context)
