# Generated by Django 4.2.6 on 2023-10-16 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bollapp', '0005_alter_fieldmodel_table_alter_reservemodel_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservemodel',
            name='day',
            field=models.DateField(),
        ),
    ]