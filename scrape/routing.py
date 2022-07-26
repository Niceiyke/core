from django.urls import path
from .consumers import ScrapeConsumer


ws_urlpatterns =[

    path('ws/scrape/', ScrapeConsumer.as_asgi())

]