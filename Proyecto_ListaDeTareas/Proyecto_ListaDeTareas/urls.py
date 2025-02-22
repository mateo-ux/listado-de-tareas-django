"""
URL configuration for Proyecto_ListaDeTareas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ListaDeTareasAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio,name = 'index'),
    path('tarea/crear/',views.tarea_crear,name = 'tarea_crear'),
    path('tareas/',views.tareas_index,name = 'tareas_index'),
    path('tarea/<int:tarea_id>/',views.tarea_actualizar,name ='tarea_actualizar'),
    path('tarea/eliminar/<int:tarea_id>',views.tarea_eliminar,name = 'tarea_eliminar'),
    path('buscar/', views.buscar_tareas, name='buscar_tareas'),
]
