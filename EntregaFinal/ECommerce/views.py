
from multiprocessing import AuthenticationError
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

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin



# Create your views here.

@login_required
def inicio(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    novedades = Novedad.objects.all

    producto = Producto.objects.all
    
    return render(request, "ECommerce/inicio.html", {"url":avatares[0].imagen.url,"novedades":novedades, "producto":producto} )

# CONTACTO.
def contacto(request):
    
    return render(request, "ECommerce/contacto.html") 

# SOBRE NOSOTROS.
def sobre_nosotros(request):
    
    return render(request, "ECommerce/sobre_nosotros.html") 

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

            user = User.objects.filter(username=username).first()
            
            cliente = Cliente(nombre=user.first_name, apellido=user.last_name, idUser=user, telefono=0,dni=0,email='agrega@tuemail.com')
            cliente.save()

            avatar = Avatar(imagen= "avatares/deffault.jpg", user_id = user.id)
            avatar.save()

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

class ClienteList(PermissionRequiredMixin, ListView):
    permission_required = 'ECommerce.view_cliente'

    model = Cliente
    template_name = "ECommerce/cliente_lista.html"

class ClienteDetalle(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name =  "ECommerce/cliente_detalle.html"

class ClienteCreacion(PermissionRequiredMixin, CreateView):
    permission_required = 'ECommerce.add_cliente'

    model = Cliente
    template_name =  "ECommerce/cliente_form.html"
    success_url = "/cliente/lista"
    fields = ["nombre", "apellido", "email", "dni", "telefono"]

class ClienteUpdate(LoginRequiredMixin, UpdateView):

    model= Cliente
    success_url = "/cliente/lista"
    fields = ["nombre", "apellido", "email", "dni", "telefono"]

class ClienteDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'ECommerce.delete_cliente'

    model = Cliente
    success_url = "/cliente/lista"

# VENDEDORES

class VendedorList(PermissionRequiredMixin, ListView):
    permission_required = 'ECommerce.view_vendedor'

    model = Vendedor
    template_name = "ECommerce/vendedor_lista.html"

class VendedorDetalle(PermissionRequiredMixin, DetailView):
    permission_required = 'ECommerce.view_vendedor'

    model = Vendedor
    template_name =  "ECommerce/vendedor_detalle.html"

class VendedorCreacion(PermissionRequiredMixin, CreateView):
    permission_required = 'ECommerce.add_vendedor'
    
    model = Vendedor
    template_name =  "ECommerce/vendedor_form.html"
    success_url = "/vendedor/lista"
    fields = ["nombre", "apellido", "email", "dni", "cuil", "salario"]

class VendedorUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'ECommerce.change_vendedor'

    model= Vendedor
    success_url = "/vendedor/lista"
    fields = ["nombre", "apellido", "email", "dni", "cuil", "salario"]

class VendedorDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'ECommerce.delete_vendedor'

    model = Vendedor
    success_url = "/vendedor/lista"

# PRODUCTOS

class ProductoList(LoginRequiredMixin, ListView):

    model = Producto
    template_name = "ECommerce/producto_lista.html"

class ProductoDetalle(LoginRequiredMixin, DetailView):
    
    model = Producto
    template_name =  "ECommerce/producto_detalle.html"

class ProductoCreacion(PermissionRequiredMixin, CreateView):
    permission_required = 'ECommerce.add_producto'
    model = Producto
    template_name =  "ECommerce/producto_form.html"
    success_url = "/producto/lista"
    fields = ["nombre", "categoria", "descripcion", "imagen", "stock", "precio"]

class ProductoUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'ECommerce.change_producto'

    model= Producto
    success_url = "/producto/lista"
    fields = ["nombre", "categoria", "descripcion", "imagen", "stock", "precio"]

class ProductoDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'ECommerce.delete_producto'

    model = Producto
    success_url = "/producto/lista"


# COMPRA

class CompraList(PermissionRequiredMixin, ListView):
    permission_required = 'ECommerce.view_compra'

    model = Compra
    template_name = "ECommerce/compra_lista.html"

class CompraDetalle(PermissionRequiredMixin, DetailView):
    permission_required = 'ECommerce.view_compra'

    model = Compra
    template_name =  "ECommerce/compra_detalle.html"

class CompraCreacion(PermissionRequiredMixin, CreateView):
    permission_required = 'ECommerce.add_compra'

    model = Compra
    template_name =  "ECommerce/compra_form.html"
    success_url = "/compra/lista"
    fields = ["idCliente", "idVendedor","direccion", "localidad", "codigoPostal", "estado", "medioPago", "fechaCompra", "fechaEnvio", "fecha", "comprobantePago"]

class CompraUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'ECommerce.change_compra'

    model= Compra
    success_url = "/compra/lista"
    fields = ["idCliente", "idVendedor","direccion", "localidad", "codigoPostal", "estado", "medioPago", "fechaCompra", "fechaEnvio", "fecha", "comprobantePago"]

class CompraDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'ECommerce.delete_compra'

    model = Compra
    success_url = "/compra/lista"


# MENSAJE

class MensajeList(LoginRequiredMixin, ListView):    

    model = Mensaje
    template_name = "ECommerce/mensaje_lista.html"

class MensajeList2(LoginRequiredMixin, ListView):    

    model = Mensaje
    template_name = "ECommerce/novedad_detalle.html"


class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name =  "ECommerce/mensaje_detalle.html"

class MensajeCreacion(LoginRequiredMixin, CreateView):
    model = Mensaje
    template_name =  "ECommerce/mensaje_form.html"
    success_url = "/mensaje/lista"
    fields = ["idMensajeAnterior", "idCliente", "idVendedor", "asunto", "mensaje", "fecha"]

class MensajeUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'ECommerce.change_mensaje'

    model= Mensaje
    success_url = "/mensaje/lista"
    fields = ["idMensajeAnterior", "idCliente", "idVendedor", "asunto", "mensaje", "fecha"]

class MensajeDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'ECommerce.delete_mensaje'

    model = Mensaje
    success_url = "/mensaje/lista"

# NOVEDAD

class NovedadList(ListView):

    model = Novedad
    template_name = "ECommerce/novedad_lista.html"
    
class NovedadDetalle(DetailView):
    model = Novedad
    template_name =  "ECommerce/novedad_detalle.html"
    
class NovedadCreacion(PermissionRequiredMixin, CreateView):
    permission_required = 'ECommerce.add_novedad'

    model = Novedad
    template_name =  "ECommerce/novedad_form.html"
    success_url = "/novedad/lista"
    fields = ["titulo", "subtitulo", "contenido", "imagen", "fecha"]
    
class NovedadUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'ECommerce.change_novedad'

    model= Novedad
    success_url = "/novedad/lista"
    fields = ["titulo", "subtitulo", "contenido", "imagen", "fecha"]

class NovedadDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'ECommerce.delete_novedad'

    model = Novedad
    success_url = "/novedad/lista"

# COMPRA X PRODUCTO

class CompraXProductoList(PermissionRequiredMixin, ListView):
    permission_required = 'ECommerce.view_compraxproducto'

    model = CompraXProducto
    template_name = "ECommerce/compraXProducto_lista.html"

class CompraXProductoDetalle(PermissionRequiredMixin, DetailView):
    permission_required = 'ECommerce.view_compraxproducto'

    model = CompraXProducto
    template_name =  "ECommerce/compraXProducto_detalle.html"

class CompraXProductoCreacion(PermissionRequiredMixin, CreateView):
    permission_required = 'ECommerce.add_compraxproducto'

    model = CompraXProducto
    template_name =  "ECommerce/compraXProducto_form.html"
    success_url = "/compraXProducto/lista"
    fields = ["idCompra", "idProducto", "cantidad", "precioTotal"]

class CompraXProductoUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'ECommerce.change_compraxproducto'

    model= CompraXProducto
    success_url = "/compraXProducto/lista"
    fields = ["idCompra", "idProducto", "cantidad", "precioTotal"]

class CompraXProductoDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'ECommerce.delete_compraxproducto'

    model = CompraXProducto
    success_url = "/compraXProducto/lista"
  
  
# NOVEDAD EN INICIO

""" class NovedadList(ListView):

    model = NovedadInicio
    template_name = "ECommerce/inicio.html"
    
class NovedadInicioDetalle(DetailView):
    model = NovedadInicio
    template_name =  "ECommerce/inicio.html"
    
class NovedadInicioCreacion(PermissionRequiredMixin, CreateView):
    permission_required = 'ECommerce.add_novedad'

    model = NovedadInicio
    template_name =  "ECommerce/inicio.html"
    success_url = "/novedad/lista2"
    fields = ["titulo", "subtitulo", "contenido", "imagen", "fecha"]
    
class NovedadInicioUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'ECommerce.change_novedad'

    model= NovedadInicio
    success_url = "/novedad/lista2"
    fields = ["titulo", "subtitulo", "contenido", "imagen", "fecha"]

class NovedadInicioDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'ECommerce.delete_novedad'

    model = NovedadInicio
    success_url = "/novedad/lista2"
 """