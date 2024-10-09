from django.urls import path
from .estudiantes import *


protagonismoViewset = ProtagonismoView.as_view({'get': 'list'})
urlpatterns = [
    path('protagonismoViewset/', protagonismoViewset, name='protagonismoViewset'),

    
]
