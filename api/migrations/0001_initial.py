# Generated by Django 4.1.6 on 2023-02-05 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntrenadorPokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('numero_medallas', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
