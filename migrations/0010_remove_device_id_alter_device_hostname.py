# Generated by Django 5.0.1 on 2024-01-09 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retia_api', '0009_rename_ipaddr_device_mgmt_ipaddr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='id',
        ),
        migrations.AlterField(
            model_name='device',
            name='hostname',
            field=models.CharField(max_length=63, primary_key=True, serialize=False),
        ),
    ]
