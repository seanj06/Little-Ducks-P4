from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.booking, name="booking"),
]