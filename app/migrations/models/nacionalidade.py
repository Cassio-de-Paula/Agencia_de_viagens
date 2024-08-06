from django.db import models

class Nacionalidade(models.TextChoices):
    ARG = 'Argentina'
    BRA = 'Brasileira'
    FRA = 'Francesa'
    URU = 'Uruguaia'
