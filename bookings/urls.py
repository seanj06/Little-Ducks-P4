from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking, name="booking"),
    path('<int:id>', views.booking_detail, name='booking_detail')
]