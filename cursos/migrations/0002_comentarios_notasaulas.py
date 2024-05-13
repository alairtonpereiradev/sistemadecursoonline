# Generated by Django 5.0.6 on 2024-05-13 17:27

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
        ('usuarios', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('data', models.DateTimeField(default=datetime.datetime.now)),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cursos.aulas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='NotasAulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(choices=[('p', 'Péssimo'), ('r', 'Ruim'), ('re', 'Regular'), ('b', 'Bom'), ('o', 'Ótimo')], max_length=50)),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cursos.aulas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario')),
            ],
        ),
    ]