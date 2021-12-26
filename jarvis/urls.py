from django.urls import path
from . import views

# URL configurations
urlpatterns = [
    path('index/', views.index),
    path('sendMessage/', views.sendMessage, name="sendMessage")
]