from asyncio.windows_events import NULL
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Usuario
from .forms import UsuarioForm

def index(request, letter=NULL):
    if letter != NULL:
        usuarios = Usuario.objects.filter(nombre__istartswith=letter)
    else:
        usuarios = Usuario.objects.filter(nombre__contains=request.GET.get('buscar', ''))

    context = {
        'usuarios': usuarios
    }

    return render(request, 'usuario/index.html', context)


def view(request, id):
    usuarios = Usuario.objects.get(id=id)

    context = {
        'usuarios': usuarios
    }

    return render(request, 'usuario/detail.html', context)


def edit(request, id):
    usuarios = Usuario.objects.get(id=id)

    if request.method == "GET":
        form = ContactoForm(instance=usuarios)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'usuario/edit.html', context)

    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuarios)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id': id
        }
        messages.success(request, 'Contacto actualizado')
        return render(request, 'usuario/edit.html', context)


def create(request):
    if request.method == "GET":
        form = UsuarioForm()
        context = {
            'form': form
        }
        return render(request, 'usuario/create.html', context)

    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('usuario')


def delete(request, id):
    usuarios = Usuario.objects.get(id=id)
    usuarios.delete()
    return redirect('usuario')

