# Generated by Django 3.2 on 2023-02-18 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebleslist_app', '0014_auto_20230218_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='comentario_user',
        ),
    ]