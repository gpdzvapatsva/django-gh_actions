from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.home, name='testing-home'),
path('', views.about, name='testing-home'),
]