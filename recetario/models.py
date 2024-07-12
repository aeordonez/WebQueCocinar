from django.db import models

# Create your models here.
class Receta(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    ingredientes = models.TextField(verbose_name="Ingredientes")
    tiempo = models.CharField(max_length=10, verbose_name="Tiempo")
    imagen = models.ImageField(upload_to="recetas")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'receta'
        verbose_name_plural = 'recetas'
        ordering = ['-created']