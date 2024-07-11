from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.Charfield(max_length=20, verbose_name ='Nombre')
    apellido  = models.Charfield(max_length=20, verbose_name ='Apellido')
    correo  = models.EmailFieldfield()
    telefono  = models.IntegerFieldield()
    
    
    def __str__(self):
        return self.nombre
    

    