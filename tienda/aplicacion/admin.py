from django.contrib import admin

# Register your models here.
from .models import *

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria")
    list_filter = ("categoria",)
    
class CompraAdmin(admin.ModelAdmin):
    list_display = ("articulo", "distribuidor")


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Cliente)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Venta)

