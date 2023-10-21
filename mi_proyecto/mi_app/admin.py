from django.contrib import admin
from .models import Repartidor, Tienda, Producto, Pago, Usuario, Cancelacion, Orden

# Register your models here.
admin.site.register(Repartidor)
admin.site.register(Tienda)
admin.site.register(Producto)
admin.site.register(Pago)
admin.site.register(Usuario)
admin.site.register(Cancelacion)
admin.site.register(Orden)
