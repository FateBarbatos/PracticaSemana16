# Generated by Django 4.2.6 on 2023-11-13 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseDeDatos', '0002_alter_asignaturas_nombre_asignatura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignaturas',
            name='Nombre_asignatura',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='carreras',
            name='Nombre_Carrera',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='Apellido_estudiante',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='Edad_estudiante',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='Nombre_estudiante',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='Apellido_profesores',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='Correo_profesores',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='Nombre_profesores',
            field=models.TextField(),
        ),
    ]