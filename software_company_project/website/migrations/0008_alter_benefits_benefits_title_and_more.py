# Generated by Django 5.1.3 on 2024-11-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefits',
            name='benefits_title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='counter',
            name='counter_heading',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='heading',
            name='heading_small_title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='heading',
            name='heading_title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='solutions',
            name='solution_title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='client_city',
            field=models.CharField(max_length=250),
        ),
    ]
