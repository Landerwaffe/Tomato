# Generated by Django 3.2.13 on 2024-01-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tomato', '0018_listing_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='pricepernight',
            field=models.IntegerField(default=None),
        ),
    ]