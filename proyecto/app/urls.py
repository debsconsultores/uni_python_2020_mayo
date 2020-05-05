from django.urls import path,include
from .views import hola_mundo

urlpatterns = [
    path('hola-mundo',hola_mundo,name="home1"),
]
