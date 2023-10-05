from django.urls import path
from mi_proyecto import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name='homepage'),
    #path funciones listado.
    path('repartidores/', views.listar_repartidores, name='nombre_url_listar_repartidores'),
    path('tiendas/', views.listar_tiendas, name='nombre_url_listar_tiendas'),
    path('productos/', views.listar_productos, name='nombre_url_listar_productos'),
    path('pagos/', views.listar_pagos, name='nombre_url_listar_pagos'),
    path('usuarios/', views.listar_usuarios, name='nombre_url_listar_usuarios'),
    path('cancelaciones/', views.listar_cancelaciones, name='nombre_url_listar_cancelaciones'),
    path('ordenes/', views.listar_ordenes, name='nombre_url_listar_ordenes'),
    #path funciones crear. 
    path('crear/repartidor/', views.crear_repartidor, name='nombre_url_crear_repartidor'),
    path('crear/tienda/', views.crear_tienda, name='crear_tienda'),
    path('crear/producto/', views.crear_producto, name='crear_producto'),
    path('crear/pago/', views.crear_pago, name='crear_pago'),
    path('crear/usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear/cancelacion/', views.crear_cancelacion, name='crear_cancelacion'),
    path('crear/orden/', views.crear_orden, name='crear_orden'),
    #path funciones para eliminar. 
    path('eliminar/repartidor/<int:id>/', views.eliminar_repartidor, name='eliminar_repartidor'),
    path('eliminar/tienda/<int:id>/', views.eliminar_tienda, name='eliminar_tienda'),
    path('eliminar/producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('eliminar/pago/<int:id>/', views.eliminar_pago, name='eliminar_pago'),
    path('eliminar/usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('eliminar/cancelacion/<int:id>/', views.eliminar_cancelacion, name='eliminar_cancelacion'),
    path('eliminar/orden/<int:id>/', views.eliminar_orden, name='eliminar_orden'),
    #path funciones para actualizar. 
    path('actualizar/repartidor/<int:id>/', views.actualizar_repartidor, name='actualizar_repartidor'),
    path('actualizar/tienda/<int:id>/', views.actualizar_tienda, name='actualizar_tienda'),
    path('actualizar/producto/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('actualizar/pago/<int:id>/', views.actualizar_pago, name='actualizar_pago'),
    path('actualizar/usuario/<int:id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('actualizar/cancelacion/<int:id>/', views.actualizar_cancelacion, name='actualizar_cancelacion'),
    path('actualizar/orden/<int:id>/', views.actualizar_orden, name='actualizar_orden'),
    
]
