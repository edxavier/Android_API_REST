from django.contrib import admin


# Register your models here.

from .models import *


@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_combo', 'vista_previa')
    #list_editable = ('nombre',)

admin.site.register(Cliente)
admin.site.register(Pedido)
#admin.site.register(DetallePedido)
admin.site.register(Comentario)
