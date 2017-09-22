from django.db import models
class persona(models.Model):
    cve_persona = models.IntegerField
    nombre = models.CharField(max_length=100)
    paterno = models.CharField(max_length=100)

class usuario(models.Model):
   cve_usuario = models.ForeignKey(persona)
   usuario = models.CharField(max_length=100)
   password = models.CharField(max_length=100)
# Create your models here.
