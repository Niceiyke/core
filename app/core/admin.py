from atexit import register
from django.contrib import admin
from .models import Results,Prediction

# Register your models here.
admin.site.register(Results)
admin.site.register(Prediction)