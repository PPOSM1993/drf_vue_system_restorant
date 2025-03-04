from django.db import models
from autoslug import AutoSlugField
from apps.categoria.models import Categoria


# Create your models here.

class Recetas(models.Model):
    # Create your models here.
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)#default=1
    nombre = models.CharField(max_length=100, null=False)
    slug = AutoSlugField(populate_from='nombre', max_length=100)
    tiempo = models.CharField(max_length=100, null=True)
    foto = models.ImageField(upload_to='recetas/', null=True, blank=True)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table='recetas'
        verbose_name='Receta'
        verbose_name_plural='Recetas'
    