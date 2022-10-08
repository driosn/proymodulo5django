from django.contrib import admin
from .models import Modulo, Estudiante, Diplomado, Calificacion, DiplomadoEstudiante

admin.site.register(Modulo)
admin.site.register(Estudiante)
admin.site.register(Diplomado)
admin.site.register(Calificacion)
admin.site.register(DiplomadoEstudiante)
