# Generated by Django 5.1.3 on 2024-11-23 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_serviceshomepagemodel_service_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceshomepagemodel',
            name='service_image',
        ),
    ]