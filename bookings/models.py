from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .book import Time_Choices
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Booking(models.Model):
    Type_of_class = (
        ("B", "Beginner"),
        ("I", "Intermediate"),
        ("A", "Advanced"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    level = models.CharField(max_length=200, choices=Type_of_class,)
    date = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=Time_Choices, default="11.00am")
    time_of_booking = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.get_level_display()
