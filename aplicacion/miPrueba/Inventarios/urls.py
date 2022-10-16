from turtle import up
from django.urls import path
from .views import index,upload,Doc
urlpatterns = [
    path('', index),
    path('/upload', upload),
    path('upload',Doc.as_view())
]
