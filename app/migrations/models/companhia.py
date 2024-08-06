from django.db import models


class Companhia(models.TextChoices):
    GOL = 'Gol'
    LAT = 'Latam'
    AZU = 'Azul'
    AAI = 'American Airlines'
    QAN = 'Qantas'
