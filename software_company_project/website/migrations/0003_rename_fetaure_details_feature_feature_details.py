# Generated by Django 5.1.3 on 2024-11-21 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_about_about_image_alter_blog_blog_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='fetaure_details',
            new_name='feature_details',
        ),
    ]
