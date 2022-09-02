from django.contrib import admin
from .models import *

admin.site.register(categoria)
admin.site.register(producto)
admin.site.register(cliente)
admin.site.register(venta)
admin.site.register(detalle_venta)