from django.contrib import admin
from django.urls import path, include
import market.views
import trends.views

urlpatterns = [
    path('', trends.views.index),
    path('mods/', trends.views.mods),
    path('textures/' trends.views.textures)
    path('skins/', trends.views.skins)
    path('games/', trends.views.games)
]
