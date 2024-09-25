from django.urls import path
from app_coder.views import *

urlpatterns = [
    path('', index, name='index'),
    path('cliente/', cliente),
    path('orden/', ordencompra),
    path('agregar-cliente/', agregar_cliente, name='agregar_cliente'),
    path('agregar-juego/', agregar_juego, name='agregar_juego'),
    path('listar-juegos/', listar_juegos, name='listar_juegos'),
    path('agregar-orden/', agregar_orden_compra, name='agregar_orden_compra'),
]