from django.contrib import admin
from app.migrations.models.passageiro import Passageiro
from app.migrations.models.voo import Voo
# Register your models here.

admin.site.register(Passageiro)
admin.site.register(Voo)