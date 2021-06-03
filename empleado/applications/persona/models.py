from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    class Meta:
        verbose_name ='Habilidad'
        verbose_name_plural ='Habilidad Empleado'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),
    ) 
    first_name =  models.CharField('Nombre', max_length=50)
    last_name =  models.CharField('Apellido', max_length=60)
    full_name =  models.CharField(
        'Nombre Completo', 
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo',max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado',blank=True,null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    
    class Meta:
        verbose_name ='Mi Nombre'
        verbose_name_plural ='Mi apellido'
        ordering =['-last_name']
        unique_together =('first_name','last_name')


    def __str__(self):
        return self.first_name + '-' + self.last_name
    
    def hability_names(self):
        return ', '.join([a.hability_name for a in self.habilidades.all()])
