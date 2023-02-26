from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .book import Time_Choices, Type_of_class


# Create your models here.

class Booking(models.Model):
    
    user = models.ForeignKey(User, default='', null=True, on_delete=models.CASCADE, related_name='user_info')
    level = models.CharField(max_length=200, choices=Type_of_class,)
    date = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=Time_Choices, default="11.00am")
    time_of_booking = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = "Booking"
    
    def __str__(self):
        return f" user: {self.user}date: {self.date} time: {self.time}"

