from django.db import models

# Create your models here.

class Tarea(models.Model):
    nombre = models.CharField(max_length = 500)
    descripcion = models.CharField(max_length = 500)
    estado = models.CharField(max_length=10, choices=[
        ('Pendiente.', 'Pendiente.'),
        ('En curso.', 'En curso.'),
        ('Terminada.', 'Terminada.'),
    ])