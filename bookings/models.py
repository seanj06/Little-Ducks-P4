from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .book import Time_Choices, Type_of_class


# Create your models here.


class Booking(models.Model):

    level = models.CharField(max_length=200, choices=Type_of_class,)
    date = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=Time_Choices, default="11.00am")
    time_of_booking = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"date: {self.date} time: {self.time}"