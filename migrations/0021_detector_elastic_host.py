# Generated by Django 5.0.1 on 2024-02-06 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retia_api', '0020_remove_detector_elastic_host_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detector',
            name='elastic_host',
            field=models.CharField(default='127.0.0.1', max_length=200),
        ),
    ]
