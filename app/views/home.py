from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
        'mensagem': 'Bem-Vindo a Decolar!'
    }
    return render(request, 'base.html', context)
