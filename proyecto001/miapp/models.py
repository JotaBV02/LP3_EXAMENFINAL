from django.db import models

# Create your models here.
class Bravo_Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    sexo = models.BooleanField()
    fecha_de_registro = models.DateField(auto_now_add=True)