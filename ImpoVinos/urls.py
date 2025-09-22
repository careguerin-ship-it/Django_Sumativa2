from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Para la landing page
    path("", views.index, name="index"),

    # Interacciones (se puede cambiar este nombre)
    path("interacciones/comprar/", views.comprar, name="comprar"),
    path("interacciones/nosotros/", views.nosotros, name="nosotros"),
    path("interacciones/contacto/", views.contacto, name="contacto"),
    path("interacciones/carrito/", views.carrito, name="carrito"),
    path("interacciones/inventario/", views.Inventario, name="inventario"),

    # Productos
    path("productos/nacionales/", views.prod_nacionales, name="nacionales"),
    path("productos/importados/", views.prod_importados, name="importados"),

    # Usuarios
    path("usuarios/ingresa/", views.ingresa, name="ingresa"),
    path("usuarios/registro/", views.registro, name="registro"),
    path("usuarios/recuperar/", views.recuperar, name="recuperar"),
    path("usuarios/perfil/", views.perfil, name="perfil"),
    path("usuarios/modificar/", views.modificarPerfil, name="modificarPerfil"),
    path("usuarios/ingresa_admin/", views.ingresa_admin, name="ingresa_admin"),

    # URL para cerrar sesión
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]