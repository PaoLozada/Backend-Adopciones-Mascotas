# Generated by Django 3.2.8 on 2021-10-22 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAdopciones', '0011_auto_20211020_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatos',
            name='Afrontar_Problemas',
            field=models.IntegerField(null=True, verbose_name='Afrontar_Problemas'),
        ),
        migrations.AlterField(
            model_name='candidatos',
            name='Has_Tenido_Mascotas',
            field=models.IntegerField(null=True, verbose_name='Ha_Tenido_Mascotas'),
        ),
        migrations.AlterField(
            model_name='candidatos',
            name='Recursos_Economicos',
            field=models.IntegerField(null=True, verbose_name='Recursos_Economicos'),
        ),
        migrations.AlterField(
            model_name='candidatos',
            name='Resultado_Prueba',
            field=models.IntegerField(null=True, verbose_name='Resultado_Prueba'),
        ),
        migrations.AlterField(
            model_name='candidatos',
            name='Seras_Responsable',
            field=models.IntegerField(null=True, verbose_name='Seras_Responsable'),
        ),
        migrations.AlterField(
            model_name='candidatos',
            name='Tienes_Espacio',
            field=models.IntegerField(null=True, verbose_name='Tienes_Espacio'),
        ),
        migrations.AlterField(
            model_name='candidatos',
            name='Tienes_Tiempo',
            field=models.IntegerField(null=True, verbose_name='Tienes_Tiempo'),
        ),
    ]