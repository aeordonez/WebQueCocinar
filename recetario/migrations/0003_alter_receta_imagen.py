# Generated by Django 5.0.6 on 2024-07-05 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetario', '0002_alter_receta_options_alter_receta_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(upload_to='recetas'),
        ),
    ]