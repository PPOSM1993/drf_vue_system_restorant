# Generated by Django 5.1.6 on 2025-03-04 15:14

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from='nombre')),
                ('tiempo', models.CharField(max_length=100, null=True)),
                ('foto', models.CharField(max_length=100, null=True)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categoria.categoria')),
            ],
            options={
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
                'db_table': 'recetas',
            },
        ),
    ]
