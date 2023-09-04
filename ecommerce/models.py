from django.db import models

# Create your models here.

class Cliente(models.Model):

    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50, default=None)
    email = models.EmailField()
    


class Pedido(models.Model):

    nro_pedido = models.IntegerField()
    forma_de_pago = models.CharField(max_length=10)
    tipo_de_pedido = models.CharField(max_length=10)


class Pickeador(models.Model):
    nombre = models.CharField(max_length=15)
    dni = models.IntegerField()
    horario = models.CharField(max_length=20)