# Generated by Django 5.0.6 on 2024-05-30 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugadores', '0002_jugador_fecha_nacimiento_jugador_ranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
