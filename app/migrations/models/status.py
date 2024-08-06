from django.db import models


class Status(models.TextChoices):
    CAN = 'Cancelado'
    DEL = 'Atrasado'
    ON = 'No horário'
