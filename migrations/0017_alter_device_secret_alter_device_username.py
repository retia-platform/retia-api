# Generated by Django 5.0.1 on 2024-01-25 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retia_api', '0016_remove_detector_device_interface_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='secret',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='device',
            name='username',
            field=models.CharField(default=None, max_length=16),
        ),
    ]
