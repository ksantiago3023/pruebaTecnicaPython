# Generated by Django 4.1.2 on 2022-10-15 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventarios', '0007_rename_fechainventario_inventario_fechainventario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='FechaInventario',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='PrecioUnidad',
            field=models.FloatField(default=0),
        ),
    ]