from django.shortcuts import render, redirect
from .forms import *

def index(request):
    return render(request, 'base.html') 

def cliente (request):

    return render (request, "cliente.html")

def juego (request):

    return render (request, "juego.html")

def ordencompra (request):

    return render (request, "orden_compra.html")

def agregar_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_juegos')
    else:
        form = JuegoForm()
    return render(request, 'agregar_juego.html', {'form': form})

def listar_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'listar_juegos.html', {'juegos': juegos}) 
    

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('index') 
    else:
        form = ClienteForm()

    return render(request, 'agregar_cliente.html', {'form': form})

def agregar_orden_compra(request):
    if request.method == 'POST':
        form = OrdenCompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrdenCompraForm()
    
    return render(request, 'agregar_orden_compra.html', {'form': form})

