
from multiprocessing import AuthenticationError
import re
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from ECommerce.models import Cliente, Vendedor,Producto ,Compra, Avatar, Mensaje, Novedad, CompraXProducto

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from ECommerce.forms import UserEditForm, AvatarFormulario

from django.contrib.auth.models import User



# Create your views here.

@login_required
def inicio(request):
    
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "ECommerce/inicio.html", {"url":avatares[0].imagen.url} )



# LOGIN y REGISTRO

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():


            datos = form.cleaned_data

            usuario = datos["username"]
            passw = datos["password"]

            user = authenticate(username=usuario, password=passw)


            if user is not None:

                login(request, user)

                return render(request, "ECommerce/inicio.html", {"mensaje":f"Bienvenido {usuario}"})

            else:

                return render(request, "ECommerce/inicio.html", {"mensaje":"Error, datos incorrectos"})

        else:

            return render(request, "ECommerce/inicio.html", {"mensaje":"Error, formulario erroneo"})

    else: 

        form = AuthenticationForm()

    return render(request, "ECommerce/login.html", {"form": form})



def registro(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "ECommerce/inicio.html" , {"mensaje": f"Usuario { username } creado"})

    else:

        form = UserCreationForm()

    return render(request, "ECommerce/registro.html", {"form":form})
    

# EDITAR PERFIL
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":

        miFormulario = UserEditForm(request.POST, request.FILES)

        if miFormulario.is_valid():


            informacion = miFormulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            
            usuario.save()
            
            return render(request, "ECommerce/inicio.html")

    else:

        miFormulario = UserEditForm(initial={"email":usuario.email})

    return render(request, "ECommerce/editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})


# Agregar Avatar

def agregarAvatar(request):
    if request.method == "POST":

        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            u = User.objects.get(username=request.user)

            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data["avatar"])

            avatar.save()

            return render(request, "ECommerce/inicio.html")
    else:

        miFormulario= AvatarFormulario()

    return render(request, "ECommerce/agregar_avatar.html", {"miFormulario":miFormulario})

# CLIENTES

class ClienteList(ListView):

    model = Cliente
    template_name = "ECommerce/cliente_lista.html"

class ClienteDetalle(DetailView):
    model = Cliente
    template_name =  "ECommerce/cliente_detalle.html"

class ClienteCreacion(CreateView):
    model = Cliente
    template_name =  "ECommerce/cliente_form.html"
    success_url = "/cliente/lista"
    fields = ["nombre", "apellido", "email", "dni", "telefono"]

class ClienteUpdate(UpdateView):

    model= Cliente
    success_url = "/cliente/lista"
    fields = ["nombre", "apellido", "email", "dni", "telefono"]

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = "/cliente/lista"

# VENDEDORES

class VendedorList(ListView):

    model = Vendedor
    template_name = "ECommerce/vendedor_lista.html"

class VendedorDetalle(DetailView):
    model = Vendedor
    template_name =  "ECommerce/vendedor_detalle.html"

class VendedorCreacion(CreateView):
    model = Vendedor
    template_name =  "ECommerce/vendedor_form.html"
    success_url = "/vendedor/lista"
    fields = ["nombre", "apellido", "email", "dni", "cuil", "salario"]

class VendedorUpdate(UpdateView):

    model= Vendedor
    success_url = "/vendedor/lista"
    fields = ["nombre", "apellido", "email", "dni", "cuil", "salario"]

class VendedorDelete(DeleteView):
    model = Vendedor
    success_url = "/vendedor/lista"

# PRODUCTOS

class ProductoList(ListView):

    model = Producto
    template_name = "ECommerce/producto_lista.html"

class ProductoDetalle(DetailView):
    model = Producto
    template_name =  "ECommerce/producto_detalle.html"

class ProductoCreacion(CreateView):
    model = Producto
    template_name =  "ECommerce/producto_form.html"
    success_url = "/producto/lista"
    fields = ["nombre", "categoria", "descripcion", "imagen", "stock", "precio"]

class ProductoUpdate(UpdateView):

    model= Producto
    success_url = "/producto/lista"
    fields = ["nombre", "categoria", "descripcion", "imagen", "stock", "precio"]

class ProductoDelete(DeleteView):
    model = Producto
    success_url = "/producto/lista"


# COMPRA

class CompraList(ListView):

    model = Compra
    template_name = "ECommerce/compra_lista.html"

class CompraDetalle(DetailView):
    model = Compra
    template_name =  "ECommerce/compra_detalle.html"

class CompraCreacion(CreateView):
    model = Compra
    template_name =  "ECommerce/compra_form.html"
    success_url = "/compra/lista"
    fields = ["idCliente", "idVendedor","direccion", "localidad", "codigoPostal", "estado", "medioPago", "fechaCompra", "fechaEnvio", "fecha", "comprobantePago"]

class CompraUpdate(UpdateView):

    model= Compra
    success_url = "/compra/lista"
    fields = ["idCliente", "idVendedor","direccion", "localidad", "codigoPostal", "estado", "medioPago", "fechaCompra", "fechaEnvio", "fecha", "comprobantePago"]

class CompraDelete(DeleteView):
    model = Compra
    success_url = "/compra/lista"


# MENSAJE

class MensajeList(ListView):

    model = Mensaje
    template_name = "ECommerce/mensaje_lista.html"

class MensajeDetalle(DetailView):
    model = Mensaje
    template_name =  "ECommerce/mensaje_detalle.html"

class MensajeCreacion(CreateView):
    model = Mensaje
    template_name =  "ECommerce/mensaje_form.html"
    success_url = "/mensaje/lista"
    fields = ["idMensajeAnterior", "idCliente", "idVendedor", "asunto", "mensaje", "fecha"]

class MensajeUpdate(UpdateView):

    model= Mensaje
    success_url = "/mensaje/lista"
    fields = ["idMensajeAnterior", "idCliente", "idVendedor", "asunto", "mensaje", "fecha"]

class MensajeDelete(DeleteView):
    model = Mensaje
    success_url = "/mensaje/lista"

# NOVEDAD

class NovedadList(ListView):

    model = Novedad
    template_name = "ECommerce/novedad_lista.html"

class NovedadDetalle(DetailView):
    model = Novedad
    template_name =  "ECommerce/novedad_detalle.html"

class NovedadCreacion(CreateView):
    model = Novedad
    template_name =  "ECommerce/novedad_form.html"
    success_url = "/novedad/lista"
    fields = ["titulo", "subtitulo", "contenido", "imagen", "fecha"]

class NovedadUpdate(UpdateView):

    model= Novedad
    success_url = "/novedad/lista"
    fields = ["titulo", "subtitulo", "contenido", "imagen", "fecha"]

class NovedadDelete(DeleteView):
    model = Novedad
    success_url = "/novedad/lista"

# COMPRA X PRODUCTO

class CompraXProductoList(ListView):

    model = CompraXProducto
    template_name = "ECommerce/compraXProducto_lista.html"

class CompraXProductoDetalle(DetailView):
    model = CompraXProducto
    template_name =  "ECommerce/compraXProducto_detalle.html"

class CompraXProductoCreacion(CreateView):
    model = CompraXProducto
    template_name =  "ECommerce/compraXProducto_form.html"
    success_url = "/compraXProducto/lista"
    fields = ["idCompra", "idProducto", "cantidad", "precioTotal"]

class CompraXProductoUpdate(UpdateView):

    model= CompraXProducto
    success_url = "/compraXProducto/lista"
    fields = ["idCompra", "idProducto", "cantidad", "precioTotal"]

class CompraXProductoDelete(DeleteView):
    model = CompraXProducto
    success_url = "/compraXProducto/lista"