from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .book import Type_of_class, Time_Choices

# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    level = models.CharField(max_length=50, choices=Type_of_class, default="Intermediate")
    date = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=Time_Choices, default="11.00am")
    time_of_booking = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} date: {self.date} time: {self.time}"
