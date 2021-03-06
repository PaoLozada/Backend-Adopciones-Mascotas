# Generated by Django 3.2.8 on 2021-10-10 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appAdopciones', '0002_auto_20211009_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidatos',
            old_name='direccion',
            new_name='Direccion',
        ),
        migrations.RenameField(
            model_name='candidatos',
            old_name='edad',
            new_name='Edad',
        ),
        migrations.RenameField(
            model_name='candidatos',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='candidatos',
            old_name='id_candidato',
            new_name='Id_Candidato',
        ),
        migrations.RenameField(
            model_name='candidatos',
            old_name='nombre_completo',
            new_name='Nombre_Completo',
        ),
        migrations.RenameField(
            model_name='candidatos',
            old_name='numero_contacto',
            new_name='Numero_Contacto',
        ),
        migrations.RenameField(
            model_name='candidatos',
            old_name='numeroIdentificacion',
            new_name='Numero_Identificacion',
        ),
        migrations.RenameField(
            model_name='candidatos',
            old_name='resutado_prueba',
            new_name='Resutado_Prueba',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='estado',
            new_name='Estado',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='mascotas',
            new_name='Id_Mascotas',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='candidatos',
            new_name='Id_Mndidatos',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='id_adopciones',
            new_name='Id_Solicitud',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='user',
            new_name='Id_User',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='respuesta',
            new_name='Respuesta',
        ),
    ]
