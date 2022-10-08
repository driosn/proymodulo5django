from rest_framework import viewsets
from rest_framework import generics
from .models import Diplomado
from .models import Modulo
from .models import Estudiante
from .models import Calificacion
from .serializers import DiplomadoSerializer,ModuloSerializer,EstudianteSerializer,CalificacionSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse

class DiplomadoViewSet(viewsets.ModelViewSet):
    queryset = Diplomado.objects.all()
    serializer_class = DiplomadoSerializer

class DiplomadoCreateAndList(generics.CreateAPIView, generics.ListAPIView):
        queryset = Diplomado.objects.all()
        serializer_class = DiplomadoSerializer

class ModuloCreateAndList(generics.CreateAPIView, generics.ListAPIView):
        queryset = Modulo.objects.all()
        serializer_class = ModuloSerializer

class EstudianteCreateAndList(generics.CreateAPIView, generics.ListAPIView):
        queryset = Estudiante.objects.all()
        serializer_class = EstudianteSerializer

class CalificacionCreateAndList(generics.CreateAPIView, generics.ListAPIView):
        queryset = Calificacion.objects.all()
        serializer_class = CalificacionSerializer

@api_view(["GET"])
def cantidad_estudiantes(request):
    """
    Cantidad de estudiantes registrados
    """
    try:
        cantidad = Estudiante.objects.count()
        return JsonResponse(
            {
                "cantidad_estudiantes": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)


