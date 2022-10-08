from django.db import models
from .validators import validar_nombre
from .validators import validar_calificacion

class Diplomado(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 
    
    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validar_nombre,]) 
    apellido = models.CharField(max_length=100, unique=True, validators =[validar_nombre,])
    
    def __str__(self):
        return self.nombre + " " + self.apellido

class Modulo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    diplomado = models.ForeignKey(Diplomado, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE) 
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE) 
    valor = models.IntegerField(validators=[validar_calificacion,])

    def __str__(self):
        return str(self.valor)

class DiplomadoEstudiante(models.Model):
    diplomado = models.ForeignKey(Diplomado, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)