from django import views
from django.contrib import admin
from django.urls import path

from ECommerce.views import ClienteList, ClienteDetalle, ClienteCreacion, ClienteDelete, ClienteUpdate
from ECommerce.views import inicio, login_request, registro, editarPerfil, agregarAvatar
from ECommerce.views import VendedorCreacion, VendedorDelete, VendedorDetalle, VendedorList, VendedorUpdate
from ECommerce.views import ProductoCreacion, ProductoDelete, ProductoDetalle, ProductoList, ProductoUpdate
from django.contrib.auth.views import LogoutView

from ECommerce.views import CompraCreacion, CompraDelete, CompraDetalle, CompraList, CompraUpdate
from ECommerce.views import MensajeCreacion, MensajeDelete, MensajeDetalle, MensajeList, MensajeUpdate
from ECommerce.views import NovedadCreacion, NovedadDelete, NovedadDetalle, NovedadList, NovedadUpdate
from ECommerce.views import CompraXProductoCreacion, CompraXProductoDelete, CompraXProductoDetalle, CompraXProductoList, CompraXProductoUpdate


urlpatterns = [

    path('', inicio, name="index"),
    path('login/', login_request, name="login"),
    path('register/', registro, name="register"),
    path('logout/', LogoutView.as_view(template_name="ECommerce/logout.html"), name="logout"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),

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

    path('compra/lista', CompraList.as_view(), name="ListaCom"),
    path('compra/detalle/<pk>', CompraDetalle.as_view(), name="DetalleCom"),
    path('compra/nuevo', CompraCreacion.as_view(), name="NuevoCom"),
    path('compra/editar/<pk>', CompraUpdate.as_view(), name="EditarCom"),
    path('compra/borrar/<pk>', CompraDelete.as_view(), name="BorrarCom"),

    path('mensaje/lista', MensajeList.as_view(), name="ListaM"),
    path('mensaje/detalle/<pk>', MensajeDetalle.as_view(), name="DetalleM"),
    path('mensaje/nuevo', MensajeCreacion.as_view(), name="NuevoM"),
    path('mensaje/editar/<pk>', MensajeUpdate.as_view(), name="EditarM"),
    path('mensaje/borrar/<pk>', MensajeDelete.as_view(), name="BorrarM"),

    path('novedad/lista', NovedadList.as_view(), name="ListaN"),
     path('novedad/lista2', NovedadList.as_view(), name="ListaN"),
    path('novedad/detalle/<pk>', NovedadDetalle.as_view(), name="DetalleN"),
    path('novedad/nuevo', NovedadCreacion.as_view(), name="NuevoN"),
    path('novedad/editar/<pk>', NovedadUpdate.as_view(), name="EditarN"),
    path('novedad/borrar/<pk>', NovedadDelete.as_view(), name="BorrarN"),

    path('compraXProducto/lista', CompraXProductoList.as_view(), name="ListaCXP"),
    path('compraXProducto/detalle/<pk>', CompraXProductoDetalle.as_view(), name="DetalleCXP"),
    path('compraXProducto/nuevo', CompraXProductoCreacion.as_view(), name="NuevoCXP"),
    path('compraXProducto/editar/<pk>', CompraXProductoUpdate.as_view(), name="EditarCXP"),
    path('compraXProducto/borrar/<pk>', CompraXProductoDelete.as_view(), name="BorrarCXP"),

]