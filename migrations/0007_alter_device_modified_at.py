# Generated by Django 5.0.1 on 2024-01-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retia_api', '0006_alter_device_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='modified_at',
            field=models.DateField(auto_now=True),
        ),
    ]