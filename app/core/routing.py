from django.urls import path
from .consumers import CoreConsumer


ws_urlpatterns =[

    path('ws/core/', CoreConsumer.as_asgi())

]