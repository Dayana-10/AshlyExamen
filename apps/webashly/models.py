from django.db import models

# Create your models here.
class tarea(models.Model):
    pk_tarea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    curso = models.CharField(max_length=50, blank=False, null=False)
    grado = models.CharField(max_length=100, blank=False, null=True)
    jornada = models.CharField(max_length=100, blank=False, null=True)
    notas = models.TextField(blank=False, null=True)
