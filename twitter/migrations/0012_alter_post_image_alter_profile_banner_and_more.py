# Generated by Django 4.2.3 on 2023-10-17 15:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0011_rename_image2_profile_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='posts_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='banner',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='banner_images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image1',
            field=models.ImageField(default='default.jpg', upload_to='profile_images/'),
        ),
    ]
