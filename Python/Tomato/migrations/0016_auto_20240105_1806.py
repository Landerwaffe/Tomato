# Generated by Django 3.2.13 on 2024-01-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tomato', '0015_auto_20240105_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='xcoordinate',
            field=models.FloatField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='listing',
            name='ycoordinate',
            field=models.FloatField(default=None, max_length=30),
        ),
    ]
