from applications.departamento.forms import NewDepartamentoForm
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

# Create your views here.
from .models import Departamento
from .forms import NewDepartamentoForm

class DepartamentoListView(ListView):
    template_name = 'departamento/lista.html'
    paginate_by = 2
    context_object_name = 'departamento'
    
    def get_queryset(self):
        palabra_clave= self.request.GET.get('kword','')
        lista = Departamento.objects.filter(
            name__icontains = palabra_clave
        )
        return lista   



class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    susccess_url = '/'

    def form_valid(self, form):
        depa = Departamento(
            name= form.cleaned_data['departamento'],
            shor_name= form.cleaned_data['shorname'],
        )
        depa.save()    
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )    



        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            
        )    
        return super(NewDepartamentoForm).form_valid(form)
