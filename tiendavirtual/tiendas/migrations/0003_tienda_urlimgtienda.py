# Generated by Django 5.1.2 on 2024-10-29 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendas', '0002_alter_tienda_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='UrlImgTienda',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]