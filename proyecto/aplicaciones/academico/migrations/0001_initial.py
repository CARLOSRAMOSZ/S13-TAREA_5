# Generated by Django 4.1.1 on 2022-09-21 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('Codigo', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('Asignatura', models.CharField(max_length=50)),
                ('Duracion', models.PositiveSmallIntegerField(default=5)),
                ('Asistencias', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
