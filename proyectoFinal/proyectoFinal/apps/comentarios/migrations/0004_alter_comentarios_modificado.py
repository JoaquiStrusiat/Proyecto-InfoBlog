# Generated by Django 4.2.3 on 2023-07-28 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_alter_comentarios_modificado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='modificado',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado'),
        ),
    ]
