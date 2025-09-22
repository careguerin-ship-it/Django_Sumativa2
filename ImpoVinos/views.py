from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        # Obtener los datos del formulario
        correo = request.POST.get('correo')
        clave = request.POST.get('clave')

        # Autenticar al usuario
        user = authenticate(request, username=correo, password=clave)
        
        if user is not None:
            # Si el usuario es válido, iniciar sesión
            login(request, user)
            messages.success(request, '¡Has iniciado sesión correctamente!')
            return redirect('index')

        else:
            # Si el usuario no es válido, mostrar un error
            messages.error(request, 'Correo o contraseña incorrectos.')
            return render(request, "usuarios/ingresa.html")
            
    else:
        # Si la solicitud es GET, simplemente muestra la página de ingreso
        return render(request, "usuarios/ingresa.html")

def registro(request):
    return render(request, "usuarios/registro.html")

def recuperar(request):
    return render(request, "usuarios/recuperar.html")

def perfil(request):
    return render(request, "usuarios/perfil.html")

def modificarPerfil(request): #aqui ojo que el html tiene una mayuscula (camelCase)
    return render(request, "usuarios/modificarPerfil.html")

def ingresa_admin(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        # Cambia 'clave' por 'password' para que coincida con tu HTML
        password = request.POST.get('password') 

        # Usa la nueva variable 'password' para autenticar
        user = authenticate(request, username=usuario, password=password)

        if user is not None:
            if user.is_superuser or user.is_staff:
                login(request, user)
                messages.success(request, '¡Has ingresado como administrador!')
                return redirect('index')
            else:
                messages.error(request, 'No tienes permisos de administrador.')
                return render(request, "usuarios/admin.html")
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return render(request, "usuarios/admin.html")
            
    return render(request, "usuarios/admin.html")

def es_admin(user):
    return user.is_superuser or user.is_staff

@user_passes_test(es_admin, login_url='/usuarios/ingresa_admin/') # Redirige si no tiene acceso
def Inventario(request):
    return render(request, "interacciones/Inventario.html")