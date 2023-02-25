from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.booking, name="booking"),
    path('bookings/booking_detail', views.booking_detail, name="booking_detail") 
]