# Generated by Django 5.0.1 on 2024-01-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retia_api', '0010_remove_device_id_alter_device_hostname'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='secret',
            field=models.CharField(default='retia00!', max_length=64),
        ),
        migrations.AddField(
            model_name='device',
            name='username',
            field=models.CharField(default='retia', max_length=16),
        ),
    ]
