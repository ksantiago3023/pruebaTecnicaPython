# Generated by Django 4.1.2 on 2022-10-15 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventarios', '0006_alter_pendientes_procesado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='fechaInventario',
            new_name='FechaInventario',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='GLN_cliente',
            new_name='GLN_Cliente',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='GLN_sucursal',
            new_name='GLN_Sucrusal',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='Gtin_producto',
            new_name='Gtin_Producto',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='inventario_final',
            new_name='Inventario_Final',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='precioUnidad',
            new_name='PrecioUnidad',
        ),
    ]
