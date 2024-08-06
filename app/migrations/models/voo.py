from app.migrations.models.base import BaseModel
from app.migrations.models.passageiro import Passageiro
from app.migrations.models.companhia import Companhia
from app.migrations.models.status import Status
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Voo(BaseModel):
    class Meta:
        abstract = False

    cod_voo = models.CharField(max_length=10, validators=[MinLengthValidator(1)], blank=False, null=False, unique=True)
    origem = models.CharField(max_length=50, validators=[MinLengthValidator(3)], blank=False, null=False)
    destino = models.CharField(max_length=50, validators=[MinLengthValidator(3)], blank=False, null=False)
    partida = models.DateTimeField()
    chegada = models.DateTimeField()
    assentos_disp = models.IntegerField(default=100)
    preco = models.FloatField(validators=[MinValueValidator(0)], blank=False, null=False)
    companhia = models.CharField(choices=[(companhia.name, companhia.value) for companhia in Companhia], max_length=15)
    duracao_voo = models.DurationField()
    status = models.CharField(choices=[(status.name, status.value) for status in Status], max_length=15)
    passageiro = models.ManyToManyField(Passageiro, blank=True)

    def __str__(self):
        return f'Vôo: {self.cod_voo}\n {self.origem} para {self.destino}\n companhia: {self.companhia}'

    def get_voos_by_companhia(self, c: Companhia):
        try:
            if isinstance(c, Companhia):
                return list(Voo.objects.filter(companhia=c))
            else:
                raise TypeError('Tipo de parâmetro inválido')
        except Exception as e:
            raise e

    def get_voos_by_origem_preco(self, o: str, p: float):
        try:
            if isinstance(o, str) and isinstance(p, float):
                if 3 <= len(o) <= 50 and p > 0:
                        return list(Voo.objects.filter(origem=o).filter(preco=p))
                else:
                    raise ValueError('Limite de caracteres não respeitado')
            else:
                raise TypeError('Tipo de parâmetro inválido')
        except Exception as e:
                        raise e

    def get_voos_by_passageiro(p: Passageiro):
        try:
            if isinstance(p, Passageiro):
                return list(Voo.objects.filter(passageiro=p))
            else:
                raise TypeError('Tipo de parâmetro inválido')
        except Exception as e:
                    raise e

    def get_voos_by_origem_status_(self, o: str, s: Status):
        try:
            if isinstance(o, str) and isinstance(s, Status):
                if 3 <= len(o) <= 50:
                    return list(Voo.objects.filter(origem=o).filter(status=s))
                else:
                    raise ValueError('Limite de caracteres não respeitado')
            else:
                raise TypeError('Tipo de parâmetro inválido')
        except Exception as e:
                        raise e



