# Generated by Django 3.0.5 on 2022-12-08 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_auto_20221208_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topping',
            old_name='review',
            new_name='topping_name',
        ),
    ]
