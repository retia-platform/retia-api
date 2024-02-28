# Generated by Django 5.0.1 on 2024-01-24 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retia_api', '0013_alter_device_port'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detector',
            fields=[
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='retia_api.device')),
                ('device_interface', models.CharField(max_length=200)),
                ('window_size', models.IntegerField()),
                ('sampling_interval', models.IntegerField()),
                ('elastic_host', models.GenericIPAddressField()),
                ('elastic_index', models.CharField(max_length=255)),
                ('filebeat_host', models.GenericIPAddressField()),
                ('filebeat_port', models.BigIntegerField()),
            ],
        ),
    ]
