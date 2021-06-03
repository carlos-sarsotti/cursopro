from django.contrib import admin
from django.urls import path
from . import views
app_name = 'persona_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    
    path('listar-todo-empleados/',
        views.ListAllEmpleados.as_view(),
        name='empleado_all'
    ),

    path('lista-empleados-admin/',
        views.ListEmpleadosAdmin.as_view(),
        name='empleado_admin'
    ),

    path(
        'listar-by-area/<shorname>',
        views.ListByAreaEmpleado.as_view(),
        name ='empleados_area'    
    ),
    
    path('listar-by-trabajo/<empljob>', views.ListByTrabajoEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosBykword.as_view()),
    path(
        'buscar-habilidades/', 
        views.ListHabilidadesEmpleados.as_view(),
        name='habilidades'
        ),
    
    path(
        'ver-empleado/<pk>',
        views.EmpleadoDetailView.as_view(),
        name ='empleado_detail'
    ),

    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name ='empleado_add'
    ),
    path('success/', views.SuccessView.as_view(), name='correcto'),

    path('update-empleado/<pk>', 
        views.EmpleadoUpdateView.as_view(),
        name ='modificar_empleado'        
    ),
    
    path('delete-empleado/<pk>', 
        views.EmpleadoDeleteView.as_view(),
        name ='eliminar_empleado'        
    ),
]
