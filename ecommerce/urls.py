from django.urls import path
from ecommerce.views import clientes, inicio, pedido, pickeador, cliente, cliente_formulario , pickeador_formulario, pedido_formulario, busqueda_pedido, buscar


urlpatterns = [
    path('clientes/', clientes , name="Clientes"),
    path('', inicio ,  name="Inicio"),
    path('pedido/', pedido, name="Pedido"),
    path('pickeador/', pickeador , name="Pickeador"),
    path('nuevo-cliente/<nombre>/<direccion>/<email>', cliente),
    path('cliente-formulario/', cliente_formulario , name="ClienteFormulario"),
    path('pickeador-formulario/', pickeador_formulario , name="PickeadorFormulario"),
    path('pedido-formulario/', pedido_formulario , name="PedidoFormulario"),
    path('buscar/', buscar , name="Buscar"),
    path('busqueda-pedido/', busqueda_pedido , name="BusquedaPedido"),





    
]