# Generated by Django 5.1.2 on 2024-11-12 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_location_address_line2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
