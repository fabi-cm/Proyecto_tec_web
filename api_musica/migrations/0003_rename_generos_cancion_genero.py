# Generated by Django 4.2.1 on 2023-05-30 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_musica', '0002_alter_cancion_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancion',
            old_name='generos',
            new_name='genero',
        ),
    ]
