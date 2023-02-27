from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from .models import Booking
from .forms import BookingForm


# Create your views here.

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid:
            form.save()
            level = form.cleaned_data['level']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            context = {
                'level': level,
                'date': date,
                'time': time,
            }
            return render(request, 'booking-conf.html', context)

    else:
        form = BookingForm()

    context = {
        "form": form,
    }
    return render(request, 'booking.html', context)


