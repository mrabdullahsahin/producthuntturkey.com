# Generated by Django 4.0 on 2022-06-28 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addyourstartup', '0004_addyourstartuparea_product_future_launch_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addyourstartuparea',
            name='product_future_launch_date',
        ),
    ]
