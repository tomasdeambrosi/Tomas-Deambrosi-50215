from django.urls import path, include
from.views import *

urlpatterns = [
    #____________ Adicionales
    path('', index, name="index"),
    path('acerca_de', acerca_de, name="acerca_de"),

    #____________ Artículos
    path('articulos/', ArticuloList.as_view(), name="articulos"),
    path('articulos_create/', ArticuloCreate.as_view(), name="articulos_create"),
    path('articulos_update/<int:pk>/', ArticuloUpdate.as_view(), name="articulos_update"),
    path('articulos_delete/<int:pk>/', ArticuloDelete.as_view(), name="articulos_delete"),

    #____________ Clientes
    path('clientes/', ClienteList.as_view(), name="clientes"),
    path('clientes_create/', ClienteCreate.as_view(), name="clientes_create"),
    path('clientes_update/<int:pk>/', ClienteUpdate.as_view(), name="clientes_update"),
    path('clientes_delete/<int:pk>/', ClienteDelete.as_view(), name="clientes_delete"),
    
    #____________ Ventas
    path('ventas/', VentaList.as_view(), name="ventas"),
    path('ventas_create/', VentaCreate.as_view(), name="ventas_create"),
    path('ventas_update/<int:pk>/', VentaUpdate.as_view(), name="ventas_update"),
    path('ventas_delete/<int:pk>/', VentaDelete.as_view(), name="ventas_delete"),
    
    #____________ Compras
    path('compras/', CompraList.as_view(), name="compras"),
    path('compras_create/', CompraCreate.as_view(), name="compras_create"),
    path('compras_update/<int:pk>/', CompraUpdate.as_view(), name="compras_update"),
    path('compras_delete/<int:pk>/', CompraDelete.as_view(), name="compras_delete"),

    #____________ Búsqueda
    path('encontrar_articulos/', encontrarArticulos, name="encontrar_articulos"),

    #___________ Login, Logout
    path('login/', login_request, name="login"),
    path('logout', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('registrar/', register, name="registrar"),

    #____________ Edición de perfil, Cambio de clave, Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]


