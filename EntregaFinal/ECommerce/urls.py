from django import views
from django.contrib import admin
from django.urls import path

from ECommerce.views import ClienteList, ClienteDetalle, ClienteCreacion, ClienteDelete, ClienteUpdate
from ECommerce.views import inicio, login_request, registro
from ECommerce.views import VendedorCreacion, VendedorDelete, VendedorDetalle, VendedorList, VendedorUpdate
from ECommerce.views import ProductoCreacion, ProductoDelete, ProductoDetalle, ProductoList, ProductoUpdate





urlpatterns = [

    path('', inicio, name="index"),
    path('login/', login_request, name="login"),
    path('register/', registro, name="register"),

    path('cliente/lista', ClienteList.as_view(), name="ListaC"),
    path('cliente/detalle/<pk>', ClienteDetalle.as_view(), name="DetalleC"),
    path('cliente/nuevo', ClienteCreacion.as_view(), name="NuevoC"),
    path('cliente/editar/<pk>', ClienteUpdate.as_view(), name="EditarC"),
    path('cliente/borrar/<pk>', ClienteDelete.as_view(), name="BorrarC"),

    path('vendedor/lista', VendedorList.as_view(), name="ListaV"),
    path('vendedor/detalle/<pk>', VendedorDetalle.as_view(), name="DetalleV"),
    path('vendedor/nuevo', VendedorCreacion.as_view(), name="NuevoV"),
    path('vendedor/editar/<pk>', VendedorUpdate.as_view(), name="EditarV"),
    path('vendedor/borrar/<pk>', VendedorDelete.as_view(), name="BorrarV"),

    path('producto/lista', ProductoList.as_view(), name="ListaP"),
    path('producto/detalle/<pk>', ProductoDetalle.as_view(), name="DetalleP"),
    path('producto/nuevo', ProductoCreacion.as_view(), name="NuevoP"),
    path('producto/editar/<pk>', ProductoUpdate.as_view(), name="EditarP"),
    path('producto/borrar/<pk>', ProductoDelete.as_view(), name="BorrarP"),

]