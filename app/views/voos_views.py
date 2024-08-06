from django.shortcuts import get_object_or_404, redirect, render
from app.migrations.models.voo import Voo
from app.migrations.models.passageiro import Passageiro
from app.forms import AddPassageiroForm, VooForm

def list_voos(request):
    try:
        if request.method == 'GET':
            voos = list(Voo.objects.all())

            context = {
                'voos': voos
            }

            return render(request, 'list_voos.html', context)
        else:
            raise Exception('Método inválido')
    except Exception as e:
        context = {
                'message': e
            }
        return render(request, 'error.html', context)

def create_voo(request):
    try:
        if request.method == 'POST':
            form = VooForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('list_voos')
            else:
                raise Exception('Formulário inválido')
        else:
            form = VooForm()
            context = {
                'form': form,
            }
            return render(request, 'create_voo.html', context)
    except Exception as e:
        context = {
                'message': e
            }
        return render(request, 'error.html', context)
    
def update_voo(request, id):
    try:
        voo = get_object_or_404(Voo, pk=id)
        if request.method == 'POST':
            if isinstance(voo, Voo):
                form = VooForm(request.post, instance=voo)
                if form.is_valid():
                    form.save()

                    return redirect('list_voos')
                else:
                    raise Exception('Formulário inválido')
            else:
                raise Exception('Instância inválida')
        else:
            form = VooForm(instance=voo)
            context = {
                'form': form,
                'voo': voo
            }
            return render(request, 'update_voo.html', context)
    except Exception as e:
        context = {
                'message': e
            }
        return render(request, 'error.html', context)
    
def delete_voo(request, id):
    try:
        voo = get_object_or_404(Voo, pk=id)
        if request.method == 'POST':
            if isinstance(voo, Voo):
                voo_id = request.POST.get('voo_id', None)
                if int(voo_id) == id:
                    voo.delete()

                    redirect('list_voos')
                else:
                    raise Exception('Id inválido')
            else:
                raise Exception('Instância inválida')
        else:
            form = VooForm()
            context = {
                'form': form,
                'voo': voo
            }
            return render(request, 'delete_voo.html', context)
    except Exception as e:
        context = {
                'message': e
            }
        return render(request, 'error.html', context)

def get_passageiros_voo(request, id):
    try:
        voo = get_object_or_404(Voo, pk=id)
        if request.method == 'GET':
            if isinstance(voo, Voo):
                tripulacao = Passageiro.get_passageiros_by_voo(voo)

                context = {
                    'tripulacao': tripulacao,
                    'voo': voo                
                }

                return render(request, 'tripulacao.html', context)
            else:
                raise Exception('Instância inválida')
        else:
            raise Exception('Método inválido')
    except Exception as e:
        context = {
            'message': str(e)
        }

        return render(request, 'error.html', context)

def add_passageiro(request, id):
    try:
        voo = get_object_or_404(Voo, pk=id)
        if request.method == 'POST':
            id = request.POST.get('passageiro', None)
            passageiro = get_object_or_404(Passageiro, pk=id)
            if isinstance(voo, Voo) and isinstance(passageiro, Passageiro):
                voo.passageiro.add(passageiro)
                voo.assentos_disp -= 1
                voo.save()

                return redirect('tripulacao', id)
            else:
                raise Exception('Instância inválida')
        else:
            form = AddPassageiroForm()
            context = {
                'form': form,
                'voo': voo
            }

            return render(request, 'add_passageiro.html', context)
    except Exception as e:
        context = {
            'message': str(e)
        }

        return render(request, 'error.html', context)

def delete_tripulante(request, passageiro_id, voo_id):
    try:
        voo = get_object_or_404(Voo, pk=voo_id)
        passageiro = get_object_or_404(Passageiro, pk=passageiro_id)
        if request.method == 'POST':
            if isinstance(voo, Voo) and isinstance(passageiro, Passageiro):
                voo.passageiro.remove(passageiro)
                voo.assentos_disp += 1
                voo.save()

                return redirect('tripulacao', voo_id)
            else:
                raise Exception('Instância inválida')
        else:
            context = {
                'passageiro': passageiro,
                'voo': voo
            }

            return render(request, 'delete_tripulante.html', context)
    except Exception as e:
        context = {
            'message': str(e)
        }

        return render(request, 'error.html', context)
            


