# Generated by Django 5.0.6 on 2024-05-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('posicion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'jugador',
                'verbose_name_plural': 'jugadores',
            },
        ),
    ]
