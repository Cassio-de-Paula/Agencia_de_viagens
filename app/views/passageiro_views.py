from django.shortcuts import get_object_or_404, render, redirect
from app.migrations.models.passageiro import Passageiro
from app.forms import PassageiroForm
from app.migrations.models.voo import Voo


def list_passageiros(request):
    try:
        if request.method == 'GET':
            passageiros = list(Passageiro.objects.all())

            context = {
                'passageiros': passageiros
            }

            return render(request, 'list_passageiros.html', context)
        else:
            raise Exception('Método inválido')
    except Exception as e:
        context = {
                'message': e
            }
        return render(request, 'error.html', context)


def create_passageiro(request):
    try:
        if request.method == 'POST':
            form = PassageiroForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('list_passageiros')
            else:
                raise Exception('Formulário inválido')
        else:
            form = PassageiroForm()
            context = {
                'form': form
            }
            return render(request, 'create_passageiro.html', context)
    except Exception as e:
        context = {
                'message': e
            }
        return render(request, 'error.html', context)

def update_passageiro(request, id):
    try:
        passageiro = get_object_or_404(Passageiro, pk=id)
        if request.method == 'POST':
            if isinstance(passageiro, Passageiro):
                form = PassageiroForm(request.POST, instance=passageiro)
                if form.is_valid():
                    form.save()

                    return redirect('list_passageiros')
                else:
                    raise Exception('Formulário inválido')
            else:
                raise Exception('Instância inválida')
        else:
            form = PassageiroForm(instance=passageiro)
            context = {
                'form': form,
                'passageiro': passageiro
            }
            return render(request, 'update_passageiro.html', context)
    except Exception as e:
        context = {
                'message': e
            }
        return render(request, 'error.html', context)

def delete_passageiro(request, id):
    try:
        passageiro = get_object_or_404(Passageiro, pk=id)
        if request.method == 'POST':
            if isinstance(passageiro, Passageiro):
                passageiro_id = request.POST.get('passageiro_id', None)
                if int(passageiro_id) == id:
                    passageiro.delete()

                    return redirect('list_passageiros')
                else:
                    raise Exception('Divergência de id')
            else:
                raise Exception('Instância inválida')
        else:
            context = {
                'passageiro': passageiro
            }
            return render(request, 'delete_passageiro.html', context)
    except Exception as e:
        context = {
                'message': e
            }
        return render(request, 'error.html', context)
    
def get_voos_passageiro(request, id):
    passageiro = get_object_or_404(Passageiro, pk=id)
    try:
        if request.method == 'GET':
            if isinstance(passageiro, Passageiro):
                lista_voos = Voo.get_voos_by_passageiro(passageiro)

                context = {
                    'lista_voos': lista_voos
                }

                return render(request, 'historico_voos.html', context)
            else:
                raise Exception('Formulário inválido')
        else:
            raise Exception('Método Inválido')
    except Exception as e:
        context = {
            'message': e
        }
        return render(request, 'error.html', context)
