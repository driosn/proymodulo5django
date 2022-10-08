from rest_framework import serializers
from .models import Diplomado
from .models import Modulo
from .models import Estudiante
from .models import Calificacion

class DiplomadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diplomado
        fields = "__all__"

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = "__all__"

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = "__all__"

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = "__all__"