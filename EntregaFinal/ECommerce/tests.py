from django.test import TestCase

from EntregaFinal.ECommerce.models import Producto

# Create your tests here.


class ProductoList(ListView):

    model = Producto
    template_name = "ECommerce/producto_lista.html"

class ProductoDetalle(DetailView):
    model = Producto
    template_name =  "ECommerce/producto_detalle.html"

class ProductoCreacion(CreateView):
    model = Producto
    template_name =  "ECommerce/producto_form.html"
    success_url = "Producto/lista"
    fields = ["nombre", "categoria", "descripcion", "imagen", "stock", "precio"]

class ProductoUpdate(UpdateView):

    model= Producto
    success_url = "/producto/lista"
    fields = ["nombre", "categoria", "descripcion", "imagen", "stock", "precio"]

class ProductoDelete(DeleteView):
    model = Producto
    success_url = "/producto/lista"