from app.migrations.models.base import BaseModel
from app.migrations.models.nacionalidade import Nacionalidade
from django.core.validators import MinLengthValidator
from django.db import models


class Passageiro(BaseModel):
    class Meta:
        abstract = False

    cod = models.CharField(max_length=10, blank=False, null=False, unique=True)
    nome = models.CharField(max_length=100, blank=False, null=False)
    data_nascimento = models.DateField()
    email = models.CharField(unique=True, max_length=100)
    telefone = models.CharField(max_length=15, validators=[MinLengthValidator(10)], blank=False, null=False)
    identidade = models.CharField(max_length=20, validators=[MinLengthValidator(4)], blank=False, null=False)
    nacionalidade = models.CharField(choices=[(nacionalidade.name, nacionalidade.value) for nacionalidade in Nacionalidade], max_length=15)
    passaporte = models.CharField(max_length=20, validators=[MinLengthValidator(5)], blank=False, null=False, unique=True)
    vencimento_passaporte = models.DateField(blank=False, null=False)
    endereco = models.CharField(max_length=50, validators=[MinLengthValidator(20)], blank=False, null=False)

    def __str__(self):
        return f'{self.nome}\n{self.nacionalidade}\npassaporte: {self.passaporte}'

    def get_passageiros_by_voo(v):
        try:
            if v.__class__.__name__ == 'Voo':
                return list(Passageiro.objects.filter(voo=v))
            else:
                raise TypeError('Tipo de parâmetro inválido')
        except Exception as e:
                raise e

    def get_passageiros_by_passaporte(self, p: str):
        try:
            if isinstance(p, str):
                if 5 <= len(p) <= 20:
                    return Passageiro.objects.get(passaporte=p)
                else:
                    raise ValueError('Limite de caracteres não respeitado')
            else:
                raise TypeError('Tipo de parâmetro inválido')
        except Exception as e:
            raise e

    def get_passageiros_by_nacionalidade(self, n: Nacionalidade):
        try:
            if isinstance(n, Nacionalidade):
                return list(Passageiro.objects.filter(nacionalidade=n))
            else:
                raise TypeError('Tipo de parâmetro inválido')
        except Exception as e:
            raise e
