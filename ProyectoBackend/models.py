from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import JSONField
from django.db import models


class UserManager(BaseUserManager):

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class Usuario(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    identificacion = models.CharField(max_length=10, unique=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField(null=True)
    genero = models.CharField(max_length=10)
    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'Usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Etapa(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'Etapa'
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    altura = models.DecimalField(max_digits=6, decimal_places=2)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    etapa = models.ManyToManyField(Etapa, through='EtapaCliente')

    class Meta:
        db_table = 'Cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class EtapaCliente(models.Model):
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)


class Area(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'Area'
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'


class Entrenador(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    area = models.ManyToManyField(Area)
    horario = JSONField(null=False, blank=False)

    class Meta:
        db_table = 'Entrenador'
        verbose_name = 'Entrenador'
        verbose_name_plural = 'Entrenadores'


class Musculo(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'Musculo'
        verbose_name = 'Musculo'
        verbose_name_plural = 'Musculos'

    def __str__(self):
        return self.nombre


class Ejercicio(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    etapas = models.ManyToManyField(Etapa, blank=True)
    musculos = models.ManyToManyField(Musculo, blank=True)

    class Meta:
        db_table = 'Ejercicio'
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'


class Rutina(models.Model):
    cliente = models.ManyToManyField(Cliente)
    dia = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    musculos = models.ManyToManyField(Musculo)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    ejercicios = JSONField(null=False, blank=False)

    class Meta:
        db_table = 'Rutina'
        verbose_name = 'Rutina'
        verbose_name_plural = 'Rutinas'


class Membresia(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=2, decimal_places=2)
    is_anulada = models.BooleanField(default=False)

    class Meta:
        db_table = 'Membresia'
        verbose_name = 'Membresia'
        verbose_name_plural = 'Membresias'
