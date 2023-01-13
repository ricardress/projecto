from django.db import models
from datetime import date

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    telefono = models.CharField(max_length=12, blank=False, null=False)
    correo = models.EmailField(blank=False, null=False)
    fecha = models.DateField(default=date.today)
    notas = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.nombre
