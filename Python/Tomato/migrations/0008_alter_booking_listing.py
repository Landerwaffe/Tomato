# Generated by Django 3.2.13 on 2024-01-01 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tomato', '0007_alter_booking_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tomato.listing'),
        ),
    ]
