# Generated by Django 4.2.6 on 2023-10-16 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bollapp', '0004_alter_reservemodel_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='fieldmodel',
            table='area',
        ),
        migrations.AlterModelTable(
            name='reservemodel',
            table='book',
        ),
    ]
