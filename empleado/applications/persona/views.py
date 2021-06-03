from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import EmpleadoForm
# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

from .models import Empleado


class InicioView(TemplateView):
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering ='first_name'
    context_object_name = 'empleado'

    def get_queryset(self):
        palabra_clave= self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave
        )
        return lista   


class ListEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering ='first_name'
    context_object_name = 'empleado'
    
    def get_queryset(self):
        palabra_clave= self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
        full_name__icontains = palabra_clave
        )
        return lista   
  

class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
        )
        return lista

class ListByTrabajoEmpleado(ListView):
    template_name = 'persona/list_by_trabajo.html'

    def get_queryset(self):
        trabajo = self.kwargs['empljob']
        lista = Empleado.objects.filter(
        job = trabajo
        )
        return lista   

class ListEmpleadosBykword(ListView):  
    #lista empleado por clave #
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleado' 

    def get_queryset(self):
        palabra_clave= self.request.GET.get('kword')
        lista = Empleado.objects.filter(
        first_name=palabra_clave
        )
        return lista   

class ListHabilidadesEmpleados(ListView):  
    #lista empleado por clave #
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades' 

    def get_queryset(self):
        #empleado = Empleado.objects.get(id=5)
        habilidad_clave= self.request.GET.get('hability')
        #print(empleado.habilidades.all())
        lista = Empleado.objects.filter(
            habilidades__id=habilidad_clave

            )
        return lista 

class EmpleadoDetailView(DetailView):
    template_name = "persona/detail_empleado.html"
    model = Empleado
    





class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleado_admin')

    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name= empleado.first_name +' '+empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    context_object_name = 'empleado' 
    fields =[
    #   ('__all__')
    'first_name',
    'last_name',
    'job',
    'departamento',
    'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleado_admin')
   # def post(self, request, *args, **kwargs):
   #     self.object = self.get_object()
   #     return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    template_name = 'persona/delete.html'
    model = Empleado
    success_url = reverse_lazy('persona_app:empleado_admin')
   # def post(self, request, *args, **kwargs):
   #     self.object = self.get_object()
   #     return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        return super(EmpleadoDeleteView, self).form_valid(form)
