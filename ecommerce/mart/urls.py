# mart/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('show/', show, name='show'),
]
