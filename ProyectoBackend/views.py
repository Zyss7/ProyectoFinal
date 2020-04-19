from rest_framework import viewsets
from .models import *
from .serializers import *

'''
class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    filterset_fields ={
        'username': ['icontains', 'exact']
    }
    ordering_fields =['username']
    ordering =['username']
'''


class EtapaViewSet(viewsets.ModelViewSet):
    serializer_class = EtapaSerializer
    queryset = Etapa.objects.all()
    filterset_fields = {
        'nombre': ['icontains', 'exact']
    }
    ordering_fields = ['nombre']
    ordering = ['nombre']


class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    filterset_fields = {
        'usuario__username': ['icontains', 'exact'],
        'usuario__identificacion': ['icontains', 'exact'],
        'etapa': ['icontains', 'exact']
    }
    # ordering_fields = ['primer_apellido']
    # ordering = ['primer_apellido']


class EtapaClienteViewSet(viewsets.ModelViewSet):
    serializer_class = EtapaClienteSerializer
    queryset = EtapaCliente.objects.all()
    filterset_fields = {
        'nombre': ['icontains'],
        'identificacion': ['icontains', 'exact'],
        'primer_apellido': ['icontains', 'exact']
    }


class AreaViewSet(viewsets.ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()
    filterset_fields = {
        'nombre': ['icontains', 'exact']
    }
    ordering_fields = ['nombre']
    ordering = ['nombre']


class EntrenadorViewSet(viewsets.ModelViewSet):
    serializer_class = EntrenadorSerializer
    queryset = Entrenador.objects.all()
    filterset_fields = {
        'usuario__username': ['icontains', 'exact'],
        'usuario__identificacion': ['icontains', 'exact'],
    }
    ordering_fields = ['usuario__primer_apellido']
    ordering = ['usuario__primer_apellido']


class MusculoViewSet(viewsets.ModelViewSet):
    serializer_class = MusculoSerializer
    queryset = Musculo.objects.all()
    filterset_fields = {
        'nombre': ['icontains', 'exact']
    }
    ordering_fields = ['nombre']
    ordering = ['nombre']


class EjercicioViewSet(viewsets.ModelViewSet):
    serializer_class = EjercicioSerializer
    queryset = Ejercicio.objects.all()
    ordering_fields = ['id', 'nombre']
    ordering = ['nombre']


class RutinaViewSet(viewsets.ModelViewSet):
    serializer_class = RutinaSerializer
    queryset = Rutina.objects.all()
    filterset_fields = {
        'musculo_id': ['exact'],
        'entrenador_id': ['exact']
    }
    ordering_fields = ['id']


class MembresiaViewSet(viewsets.ModelViewSet):
    serializer_class = MembresiaSerializer
    queryset = Membresia.objects.all()
    filterset_fields = {
        'tipo': ['icontains', 'exact'],
        'cliente_id': ['exact']
    }
    ordering_fields = ['cliente_id', 'tipo', 'estado']
    ordering = ['estado', 'cliente_id']
