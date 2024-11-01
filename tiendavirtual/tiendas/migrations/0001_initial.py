# Generated by Django 5.1.2 on 2024-10-25 23:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTienda', models.CharField(max_length=100)),
                ('descripcionTienda', models.CharField(max_length=255)),
                ('direccionTienda', models.CharField(max_length=100)),
                ('telefonoTienda', models.CharField(max_length=25)),
                ('estadoTienda', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tienda',
            },
        ),
    ]
