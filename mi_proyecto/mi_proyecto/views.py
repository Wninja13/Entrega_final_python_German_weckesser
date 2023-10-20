from django.shortcuts import render, get_object_or_404, redirect
from mi_app.models import Repartidor, Tienda, Producto, Pago, Usuario, Cancelacion, Orden
from mi_app.forms import RepartidorForm, TiendaForm, ProductoForm, PagoForm, UsuarioForm, CancelacionForm, OrdenForm,LoginForm
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from mi_app.forms import LoginForm 
from mi_app.forms import PerfilForm
from django.contrib.auth import logout
from django.shortcuts import redirect

#homepage
def homepage(request): 
    return render(request, 'homepage.html')

#Login usuarios y creación. 
def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Crear una instancia del formulario con los datos del POST
        if form.is_valid():
            username = form.cleaned_data['login_username']
            password = form.cleaned_data['login_password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = LoginForm()  # Crear una instancia vacía del formulario si no es una solicitud POST
    
    return render(request, 'login_usuarios.html', {'form': form})

def editar_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            # Redirige a una página de éxito o a donde desees después de editar el perfil
            return redirect('perfil_exitoso')  # Reemplaza 'perfil_exitoso' con el nombre de tu URL de éxito
    else:
        form = PerfilForm(instance=request.user.profile)

    return render(request, 'nombre_template_editar_perfil.html', {'form': form})

def editar_perfil(request):
    # Recupera el perfil del usuario actual
    perfil = request.user.profile

    if request.method == 'POST':
        # Si se envía un formulario, procesa los datos
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('nombre_template_crear_usuario')  # Reemplaza 'nombre_template_crear_usuario' con la URL a la vista de perfil
    else:
        # Si es una solicitud GET, muestra el formulario para editar el perfil
        form = PerfilForm(instance=perfil)

    return render(request, 'nombre_template_editar_perfil.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    # Redirecciona a la página de inicio o a donde desees después de cerrar sesión
    return redirect('nombre_de_la_vista_o_URL')

#Funciones de listado de los modelos. 
def listar_repartidores(request):
    query = request.GET.get('q')
    repartidores = Repartidor.objects.all()

    if query:
        repartidores = repartidores.filter(
            Q(nombre_apellido_repartidor__icontains=query) |
            Q(mail_repartidor__icontains=query) |
            Q(direccion_repartidor__icontains=query)
        )
    context = {
        'repartidores': repartidores,
        'is_query_empty': not query,
        'is_query_unsuccessful': query and not repartidores.exists()
    }
    
    return render(request, 'nombre_template_listar_repartidores.html', context)

def listar_tiendas(request):
    query = request.GET.get('q')
    tiendas = Tienda.objects.all()

    if query:
        tiendas = tiendas.filter(
            Q(titular_tienda__icontains=query) |
            Q(denominacion_social_tienda__icontains=query) |
            Q(direccion_tienda__icontains=query) |
            Q(telefono_tienda__icontains=query) |  
            Q(zona_tienda__icontains=query) |
            Q(mail_tienda__icontains=query)
        )

    context = {
        'tiendas': tiendas,
        'is_query_empty': not query,
        'is_query_unsuccessful': query and not tiendas.exists()
    }
    
    return render(request, 'nombre_template_listar_tiendas.html', context)

def listar_productos(request):
    query = request.GET.get('q')
    productos = Producto.objects.all()

    if query:
        productos = productos.filter(
            Q(nombre_producto__icontains=query) |
            Q(precio__iexact=query) |
            Q(categoria__icontains=query)
        )

    context = {
        'productos': productos,
        'is_query_empty': not query,
        'is_query_unsuccessful': query and not productos.exists()
    }
    
    return render(request, 'nombre_template_listar_productos.html', context)

def listar_pagos(request):
    query = request.GET.get('q')
    pagos = Pago.objects.all()

    if query:
        pagos = pagos.filter(
            Q(metodo_pago__icontains=query) |
            Q(monto__iexact=query) | 
            Q(fecha_pago__icontains=str(query))
        )

    context = {
        'pagos': pagos,
        'is_query_empty': not query,
        'is_query_unsuccessful': query and not pagos.exists()
    }
    
    return render(request, 'nombre_template_listar_pagos.html', context)

def listar_usuarios(request):
    query = request.GET.get('q')
    usuarios = Usuario.objects.all()

    if query:
        usuarios = usuarios.filter(
            Q(nombre_apellido_usuario__icontains=query) |
            Q(mail_usuario__icontains=query) |
            Q(direccion_usuario__icontains=query)
        )  # <- Cierre del paréntesis

    context = {
        'usuarios': usuarios,
        'is_query_empty': not query,
        'is_query_unsuccessful': query and not usuarios.exists()
    }

    return render(request, 'nombre_template_listar_usuarios.html', context)

def listar_cancelaciones(request):
    cancelaciones = Cancelacion.objects.all()
    return render(request, 'nombre_template_listar_cancelaciones.html', {'cancelaciones': cancelaciones})

def listar_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'nombre_template_listar_ordenes.html', {'ordenes': ordenes})
#Fin seccion de listado de modelos. 

#Funciones de creacion de modelos. 
def crear_repartidor(request):
    if request.method == "POST":
        form = RepartidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_repartidores')
    else:
        form = RepartidorForm()
    return render(request, 'nombre_template_crear_repartidor.html', {'form': form})

def crear_tienda(request):
    if request.method == "POST":
        form = TiendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_tiendas')
    else:
        form = TiendaForm()
    return render(request, 'nombre_template_crear_tienda.html', {'form': form})

def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'nombre_template_crear_producto.html', {'form': form})

def crear_pago(request):
    if request.method == "POST":
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_pagos')
    else:
        form = PagoForm()
    return render(request, 'nombre_template_crear_pago.html', {'form': form})

def crear_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'nombre_template_crear_usuario.html', {'form': form})

def crear_cancelacion(request):
    if request.method == "POST":
        form = CancelacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_cancelaciones')
    else:
        form = CancelacionForm()
    return render(request, 'nombre_template_crear_cancelacion.html', {'form': form})

def crear_orden(request):
    if request.method == "POST":
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_ordenes')
    else:
        form = OrdenForm()
    return render(request, 'nombre_template_crear_orden.html', {'form': form})
#Fin seccion funciones de creacion. 

#funciones de eliminacion. 
# Función de eliminación para el modelo Repartidor
def eliminar_repartidor(request, id):
    repartidor = get_object_or_404(Repartidor, id=id)
    if request.method == "POST":
        repartidor.delete()
        return redirect('nombre_url_listar_repartidores')
    return render(request, 'nombre_template_eliminar_repartidor.html', {'repartidor': repartidor})

# Función de eliminación para el modelo Tienda
def eliminar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id=id)
    if request.method == "POST":
        tienda.delete()
        return redirect('nombre_url_listar_tiendas')
    return render(request, 'nombre_template_eliminar_tienda.html', {'tienda': tienda})

# Función de eliminación para el modelo Producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
        return redirect('nombre_url_listar_productos')
    return render(request, 'nombre_template_eliminar_producto.html', {'producto': producto})

# Función de eliminación para el modelo Pago
def eliminar_pago(request, id):
    pago = get_object_or_404(Pago, id=id)
    if request.method == "POST":
        pago.delete()
        return redirect('nombre_url_listar_pagos')
    return render(request, 'nombre_template_eliminar_pago.html', {'pago': pago})

# Función de eliminación para el modelo Usuario
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == "POST":
        usuario.delete()
        return redirect('nombre_url_listar_usuarios')
    return render(request, 'nombre_template_eliminar_usuario.html', {'usuario': usuario})

# Función de eliminación para el modelo Cancelacion
def eliminar_cancelacion(request, id):
    cancelacion = get_object_or_404(Cancelacion, id=id)
    if request.method == "POST":
        cancelacion.delete()
        return redirect('nombre_url_listar_cancelaciones')
    return render(request, 'nombre_template_eliminar_cancelacion.html', {'cancelacion': cancelacion})

# Función de eliminación para el modelo Orden
def eliminar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == "POST":
        orden.delete()
        return redirect('nombre_url_listar_ordenes')
    return render(request, 'nombre_template_eliminar_orden.html', {'orden': orden})
#fin seccion eliminacion. 

#inicio seccion funciones actualización. 
#Actualización repartidor
def actualizar_repartidor(request, id):
    repartidor = get_object_or_404(Repartidor, id=id)
    if request.method == "POST":
        form = RepartidorForm(request.POST, instance=repartidor)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_repartidores')
    else:
        form = RepartidorForm(instance=repartidor)
    return render(request, 'nombre_template_actualizar_repartidor.html', {'form': form})

#Actualización Tienda
def actualizar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id=id)
    if request.method == "POST":
        form = TiendaForm(request.POST, instance=tienda)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_tiendas')
    else:
        form = TiendaForm(instance=tienda)
    return render(request, 'nombre_template_actualizar_tienda.html', {'form': form})

#Actualización producto
def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'nombre_template_actualizar_producto.html', {'form': form})

# Actualización Pago
def actualizar_pago(request, id):
    pago = get_object_or_404(Pago, id=id)
    if request.method == "POST":
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_pagos')
    else:
        form = PagoForm(instance=pago)
    return render(request, 'nombre_template_actualizar_pago.html', {'form': form})

# Actualización Usuario
def actualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'nombre_template_actualizar_usuario.html', {'form': form})

# Actualización Cancelacion
def actualizar_cancelacion(request, id):
    cancelacion = get_object_or_404(Cancelacion, id=id)
    if request.method == "POST":
        form = CancelacionForm(request.POST, instance=cancelacion)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_cancelaciones')
    else:
        form = CancelacionForm(instance=cancelacion)
    return render(request, 'nombre_template_actualizar_cancelacion.html', {'form': form})

# Actualización Orden
def actualizar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == "POST":
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('nombre_url_listar_ordenes')
    else:
        form = OrdenForm(instance=orden)
    return render(request, 'nombre_template_actualizar_orden.html', {'form': form})