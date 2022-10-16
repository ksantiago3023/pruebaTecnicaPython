# Generated by Django 4.1.2 on 2022-10-12 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('GLN', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('Gtin', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('GLN', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInventario', models.DateField()),
                ('inventario_final', models.IntegerField(default=0)),
                ('precioUnidad', models.IntegerField(default=0)),
                ('GLN_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventarios.clientes')),
                ('GLN_sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventarios.sucursal')),
                ('Gtin_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventarios.producto')),
            ],
        ),
    ]
