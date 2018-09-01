from django.contrib import admin
from django.urls import path, include
import textures.views

urlpatterns = [
    path('', textures.views.index),
]
