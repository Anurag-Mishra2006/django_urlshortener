from django.urls import path
from .views import create_short_url, redirect_url, home

urlpatterns = [
    path('', home),  # 👈 homepage
    path('api/shorten/', create_short_url),
    path('<str:code>/', redirect_url),
]