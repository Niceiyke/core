from datetime import date
from django.db import models

# Create your models here.

class Results (models.Model):
    home_team =models.CharField(max_length=50)
    away_team =models.CharField(max_length=50)
    ftr =models.CharField(max_length=1)
    country =models.CharField(max_length=50)
    date =models.FloatField()
    fthg =models.IntegerField()
    ftag =models.IntegerField()
    hthg =models.IntegerField(default=0)
    htag = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.country}-{self.home_team}-{self.away_team}'



class Prediction(models.Model):
    date = models.DateTimeField()
    league =models.CharField(max_length=50)
    fixture =models.CharField(max_length=50)
    home_win =models.IntegerField()
    draw =models.IntegerField()
    away_win =models.IntegerField()
    home_form =models.IntegerField()
    away_form =models.IntegerField()

    def __str__(self):
        return self.fixture

    class Meta:
        ordering = ['date','-home_win', '-away_win']

