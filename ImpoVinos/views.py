from django.shortcuts import render

# Create your views here.

# Home / landing page
def index(request):
    return render(request, "index.html")

# Interacciones (nuevamente, se puede cambiar el nombre de esta folder)
def comprar(request):
    return render(request, "interacciones/comprar.html")

def nosotros(request):
    return render(request, "interacciones/nosotros.html")

def contacto(request):
    return render(request, "interacciones/contacto.html")

def carrito(request):
    return render(request, "interacciones/carrito.html")

def Inventario(request):
    return render(request, "interacciones/Inventario.html")

# Productos
def prod_nacionales(request):
    return render(request, "productos/nacionales.html")

def prod_importados(request):
    return render(request, "productos/importados.html")

# Usuarios
def ingresa(request):
    return render(request, "usuarios/ingresa.html")

def registro(request):
    return render(request, "usuarios/registro.html")

def recuperar(request):
    return render(request, "usuarios/recuperar.html")

def perfil(request):
    return render(request, "usuarios/perfil.html")

def modificarPerfil(request): #aqui ojo que el html tiene una mayuscula (camelCase)
    return render(request, "usuarios/modificarPerfil.html")