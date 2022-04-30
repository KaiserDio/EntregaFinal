
from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from ECommerce.models import Cliente
from ECommerce.models import Vendedor
from ECommerce.models import Producto

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def inicio(request):
    
    return render(request, "ECommerce/inicio.html" )



# LOGIN y REGISTRO

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            """ usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password") """

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