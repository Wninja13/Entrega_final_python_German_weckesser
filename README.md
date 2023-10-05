# Django Rappi.

## Índice

- [Django Rappi.](#django-rappi)
  - [Índice](#índice)
  - [1.- Introducción.](#1--introducción)
  - [2.- Requisitos](#2--requisitos)
  - [3.- Instalación y Configuración](#3--instalación-y-configuración)
  - [4.- Uso](#4--uso)
  - [5.- Funcionalidades](#5--funcionalidades)
  - [6.- Contacto](#6--contacto)

## 1.- Introducción.

Este proyecto tiene por finalidad poner a prueba las utilidades que posee Django en lo que hace al desarrollo web y gestión de base de datos. A los efectos de cumplir con esto, se ha tomado como base la empresa de reparto Rappi.

## 2.- Requisitos

- Python 3.11.6
- Django 4.2.5
- Db.sqlite3
  

## 3.- Instalación y Configuración

3.1.- **Clonar el Repositorio**
    
    git clone https://github.com/Wninja13/pre_entrega_3_django.git
    cd pre_entrega_3_django\mi_proyecto
    git checkout Navbar-terminado

**Es importante mencionar que debe hacerse los siguientes pasos para poder utilizar el último código:** 

    1.- Debe clonarse el repositorio con el link anterior. 
    2.- utilizamos el comando $ git ckeckout Navbar-terminado. De esta manera se copiaran los archivos de la rama.
   

3.2.- **Configurar el entorno virtual**
    
    Para configurar el entorno virtual debe seguirse los siguientes pasos:
    - python -m venv venv
    - source venv/bin/activate  # En Windows: venv\Scripts\activate
    

3.3.- **Instalar las dependencias**
    
    En cd pre_entrega_3_django\mi_proyecto pip install django.
    

3.4.- **Realizar las migraciones**
    
    En cd pre_entrega_3_django\mi_proyecto python manage.py migrate
    

## 4.- Uso

4.1.- **Iniciar el servidor de desarrollo**
    
    En cd pre_entrega_3_django\mi_proyecto python manage.py runserver
    

4.2.- **Abre tu navegador y navega a:** 
`http://127.0.0.1:8000/`

## 5.- Funcionalidades

Para ejecutar las funcionalidades:

5.1.- **Homepage**:
    - Se observa la funcionalidad del navbar con menús desplegables en cada categoría.
    - Solo es funcional la sección "Repartidores" y sus subsecciones "Listar" y "Actualizar".

5.2.- **Repartidores - Listar**:
    - Visualización de repartidores cargados en la base de datos.
    - Búsqueda y filtrado de repartidores.
    - Visualización en forma de tarjetas. Si no hay repartidores, se pueden agregar.

5.3.- **Repartidores - Crear**:
    - Formulario para agregar un nuevo repartidor.
    - Opciones para guardar datos o volver al listado.

> **Nota**: Se utiliza herencia en el navbar y en el body del proyecto.La plantilla madre es plantilla_base.html

## 6.- Contacto

**Este proyecto está siendo desarrollado por:**

- Nombre: German G. Weckesser (Wninja.13)
- Correo electrónico: german.weckesser@gmail.com