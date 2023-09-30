from django.shortcuts import render, get_object_or_404, redirect
from mi_app.models import Repartidor, Tienda, Producto, Pago, Usuario, Cancelacion, Orden
from mi_app.forms import RepartidorForm, TiendaForm, ProductoForm, PagoForm, UsuarioForm, CancelacionForm, OrdenForm

#Funciones de listado de los modelos. 
def listar_repartidores(request):
    repartidores = Repartidor.objects.all()
    return render(request, 'nombre_template_listar_repartidores.html', {'repartidores': repartidores})

def listar_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'nombre_template_listar_tiendas.html', {'tiendas': tiendas})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'nombre_template_listar_productos.html', {'productos': productos})

def listar_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'nombre_template_listar_pagos.html', {'pagos': pagos})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'nombre_template_listar_usuarios.html', {'usuarios': usuarios})

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

#Seccion funciones de visualización. 
#Visualización repartidor
def visualizar_repartidor(request, id):
    repartidor = get_object_or_404(Repartidor, id=id)
    return render(request, 'nombre_template_visualizar_repartidor.html', {'repartidor': repartidor})

#Visualización Tienda
def visualizar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id=id)
    return render(request, 'nombre_template_visualizar_tienda.html', {'tienda': tienda})

#Visualización Producto. 
def visualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'nombre_template_visualizar_producto.html', {'producto': producto})

#Visualización Pago. 
def visualizar_pago(request, id):
    pago = get_object_or_404(Pago, id=id)
    return render(request, 'nombre_template_visualizar_pago.html', {'pago': pago})

#Visualización Usuario. 
def visualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, 'nombre_template_visualizar_usuario.html', {'usuario': usuario})

#Visualización Cancelación 
def visualizar_cancelacion(request, id):
    cancelacion = get_object_or_404(Cancelacion, id=id)
    return render(request, 'nombre_template_visualizar_cancelacion.html', {'cancelacion': cancelacion})

#Visualización Orden 
def visualizar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)
    return render(request, 'nombre_template_visualizar_orden.html', {'orden': orden})
#Fin sección funciones visualización. 

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