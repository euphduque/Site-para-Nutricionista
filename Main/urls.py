from django.contrib import admin
from django.urls import path, include

from Main.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
