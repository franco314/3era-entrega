from django import forms

class ClienteFormulario (forms.Form):
    nombre = forms.CharField(required=True)
    direccion = forms.CharField(required=True)
    mail = forms.EmailField()


class PickeadorFormulario (forms.Form):
    nombre = forms.CharField(max_length=15)
    dni = forms.IntegerField()
    horario = forms.CharField(max_length=20)


class PedidoFormulario (forms.Form):
    nro_pedido = forms.IntegerField()
    forma_de_pago = forms.CharField(max_length=10)
    tipo_de_pedido = forms.CharField(max_length=10)