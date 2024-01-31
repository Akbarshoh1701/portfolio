# Generated by Django 5.0.1 on 2024-01-31 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolo_app', '0008_alter_contact_call_alter_testimonials_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='img',
            field=models.ImageField(upload_to='static/assets/img/portfolio'),
        ),
        migrations.AlterField(
            model_name='typeservice',
            name='img',
            field=models.CharField(choices=[('col-lg-4 col-md-6 icon-box', 'Lorem Ipsum'), ('col-lg-4 col-md-6 icon-box', 'pitichka'), ('col-lg-4 col-md-6 icon-box', 'antina'), ('col-lg-4 col-md-6 icon-box', 'durben'), ('col-lg-4 col-md-6 icon-box', 'quyosh'), ('col-lg-4 col-md-6 icon-box', 'kalindar')], max_length=255),
        ),
    ]
