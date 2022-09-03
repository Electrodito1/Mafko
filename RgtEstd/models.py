from django.db import models

# Create your models here.

class Formulario(models.Model):
    usuario =models.CharField(max_length=20,primary_key=True)
    nombre = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    correo = models.CharField(max_length=35)
    telefono = models.CharField(max_length=10)
    class Meta:
        db_table='formulario'
