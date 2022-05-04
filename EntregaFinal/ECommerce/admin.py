from django.contrib import admin
from .models import Avatar, Cliente, Vendedor, Producto, Compra, CompraXProducto, Mensaje, Novedad

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(CompraXProducto)
admin.site.register(Mensaje)
admin.site.register(Novedad)

admin.site.register(Avatar)