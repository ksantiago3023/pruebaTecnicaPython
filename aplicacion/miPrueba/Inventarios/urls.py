from turtle import up
from django.urls import path
from .views import index,upload
urlpatterns = [
    path('', index),
    path('/upload', upload)
]
