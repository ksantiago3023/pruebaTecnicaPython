# Generated by Django 4.1.2 on 2022-10-13 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pendientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_s3', models.CharField(max_length=100)),
                ('procesado', models.BooleanField(default=False)),
            ],
        ),
    ]
