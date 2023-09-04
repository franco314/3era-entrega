from django.http import HttpResponse , HttpRequest
from django.shortcuts import render
from .models import Cliente, Pickeador, Pedido 
from .forms import ClienteFormulario , PickeadorFormulario, PedidoFormulario




def cliente(req, nombre, direccion, mail) :
    cliente = Cliente(nombre=nombre, direccion=direccion, mail=mail)
    cliente.save()
    return HttpResponse(f"""
                        <p>Hola {cliente.nombre} tus datos fueron ingresados con exito.<p>
                      """  )





def inicio(req):

   return render(req, "inicio.html")


def pedido(req):

   return render(req, "pedido.html")


def pickeador(req):

   return render(req, "pickeador.html")

def clientes(req):

   return render(req, "clientes.html")



def cliente_formulario (request: HttpRequest):
  print('method' , request.method)
  print('post' , request.POST)

  if request.method =='POST':
     
     miFormulario = ClienteFormulario(request.POST)

     if miFormulario.is_valid():
        
        print(miFormulario.cleaned_data)
        data = miFormulario.cleaned_data

        cliente = Cliente(nombre=data["nombre"], direccion=data["direccion"])
        cliente.save()
        return render(request, "inicio.html", {"mensaje": "Cliente creado con exito"})
     else: 
        return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
     
  else:
      miFormulario = ClienteFormulario()
      return render(request, "cliente_formulario.html" , {"miFormulario": miFormulario})  
   

def pickeador_formulario (request: HttpRequest):
  print('method' , request.method)
  print('post' , request.POST)

  if request.method =='POST':
     
     miFormulario = PickeadorFormulario(request.POST)

     if miFormulario.is_valid():
        
        print(miFormulario.cleaned_data)
        data = miFormulario.cleaned_data

        pickeador = Pickeador(nombre=data["nombre"], dni=data["dni"], horario=data["horario"])
        pickeador.save()
        return render(request, "inicio.html", {"mensaje": "Pedido asignado con exito"})
     else: 
        return render(request, "inicio.html", {"mensaje": "Pedido asignado con exito"})
     
  else:
      miFormulario = PickeadorFormulario()
      return render(request, "pickeador_formulario.html" , {"miFormulario": miFormulario})   
  

def pedido_formulario (request: HttpRequest):
  print('method' , request.method)
  print('post' , request.POST)

  if request.method =='POST':
     
     miFormulario = PedidoFormulario(request.POST)

     if miFormulario.is_valid():
        
        print(miFormulario.cleaned_data)
        data = miFormulario.cleaned_data

        pedido = Pedido(nro_pedido=data["nro_pedido"], forma_de_pago=data["forma_de_pago"], tipo_de_pedido=data["tipo_de_pedido"])
        pedido.save()
        return render(request, "inicio.html", {"mensaje": "Su pedido esta en camino"})
     else: 
        return render(request, "inicio.html", {"mensaje": "datos incorrectos"})
     
  else:
      miFormulario = PedidoFormulario()
      return render(request, "pedido_formulario.html" , {"miFormulario": miFormulario})    
  

def buscar (req):

     if req.GET["nro_pedido"]:
        nro_pedido = req.GET["nro_pedido"]
        pedido = Pedido.objects.get(nro_pedido=nro_pedido)
        if pedido:
            return render(req, "resultadoPedido.html" , {"pedido": pedido})
     else:
         return HttpResponse("No escribiste ningun pedido")

    
    
def busqueda_pedido (req):
   return render (req, "busquedaPedido.html")