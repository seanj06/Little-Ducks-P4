from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Person(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title
