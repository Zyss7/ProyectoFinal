from pkg_resources import require
from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS
from .models import *


class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    fecha_nacimiento = serializers.DateField(required=False)

    class Meta:
        model = Usuario
        exclude = ('password',)


class EtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields = ALL_FIELDS


class ClienteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    etapa = EtapaSerializer(many=True, required=False)

    class Meta:
        model = Cliente
        fields = ALL_FIELDS

    def create(self, validated_data):
        usuario_dict = validated_data.pop('usuario')

        usuario = Usuario(**usuario_dict)
        usuario.username = usuario.identificacion
        usuario.set_password('123456')
        usuario.save()

        cliente = Cliente(**validated_data)
        cliente.usuario = usuario
        cliente.save()
        return cliente


class EtapaClienteSerializer(serializers.ModelSerializer):
    etapa = EtapaSerializer(read_only=True)
    cliente = ClienteSerializer(read_only=True)

    class Meta:
        model = EtapaCliente
        fields = ALL_FIELDS


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ALL_FIELDS


class EntrenadorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(required=False)
    area = AreaSerializer(many=True, required=False)
    horario = serializers.JSONField(required=False)

    class Meta:
        model = Entrenador
        fields = ALL_FIELDS

    def create(self, validated_data):
        usuario_dict = validated_data.pop('usuario')

        usuario = Usuario(**usuario_dict)
        usuario.username = usuario.identificacion
        usuario.set_password('123456')
        usuario.save()

        entrenador = Entrenador(**validated_data)
        entrenador.usuario = usuario

        entrenador.save()
        return entrenador


class MusculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musculo
        fields = ALL_FIELDS


class EjercicioSerializer(serializers.ModelSerializer):
    etapas_array = EtapaSerializer(
        many=True, source='etapas',
        read_only=True,

    )
    musculos_array = MusculoSerializer(
        many=True, source='musculos',
        read_only=True
    )

    class Meta:
        model = Ejercicio
        fields = ALL_FIELDS
        extra_kwargs = {
            'etapas': {'write_only': True, 'required': False},
            'musculos': {'write_only': True, 'required': False},
        }


class RutinaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(many=True)
    musculo = MusculoSerializer(many=True)
    entrenador = EntrenadorSerializer(read_only=True)

    class Meta:
        model = Rutina
        fields = ALL_FIELDS


class MembresiaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)

    class Meta:
        model = Membresia
        fields = ALL_FIELDS
