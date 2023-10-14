from django.contrib.auth.models import Group, Permission
from mi_app.models import (Repartidor, Tienda, Producto, Pago, Usuario, Cancelacion, Orden)

def create_groups_and_permissions():
    # Crear grupo "Observador"
    observador_group, created = Group.objects.get_or_create(name='Observador')
    # No necesita permisos específicos porque solo observará la información

    # Crear grupo "Editor"
    editor_group, created = Group.objects.get_or_create(name='Editor')

    # Modelos para los cuales deseamos gestionar permisos
    models = [Repartidor, Tienda, Producto, Pago, Usuario, Cancelacion, Orden]

    for model in models:
        model_name = model._meta.model_name  # Obtener el nombre del modelo de forma dinámica
        
        # Asignamos permisos de agregar y cambiar para cada modelo al grupo "Editor"
        add_perm = Permission.objects.get(codename=f'add_{model_name}', content_type__app_label='mi_app')
        change_perm = Permission.objects.get(codename=f'change_{model_name}', content_type__app_label='mi_app')

        editor_group.permissions.add(add_perm, change_perm)

    print("Grupos y permisos creados con éxito para todos los modelos.")

