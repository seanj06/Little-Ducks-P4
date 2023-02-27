from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField
from bookings.models import Booking

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    about = models.TextField()
    avatar = CloudinaryField('image')
    bookings = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

