# Generated by Django 3.2.13 on 2024-01-09 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tomato', '0020_alter_listing_pricepernight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='pricepernight',
            field=models.IntegerField(default=None),
        ),
    ]
