# Generated by Django 3.2.13 on 2023-12-31 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tomato', '0002_auto_20231229_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=models.SlugField(),
        ),
    ]
