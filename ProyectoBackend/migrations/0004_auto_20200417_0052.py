# Generated by Django 3.0.3 on 2020-04-17 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoBackend', '0003_entrenador_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ejercicio',
            old_name='etapa',
            new_name='etapas',
        ),
    ]
