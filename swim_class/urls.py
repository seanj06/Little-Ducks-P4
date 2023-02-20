from django.urls import path
from swim_class.views import home

urlpatterns = [
    path("", home, name="home")
]