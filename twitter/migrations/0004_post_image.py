# Generated by Django 4.2.5 on 2023-09-28 12:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', null=b'I01\n', upload_to='photo/%Y/%m/%d.jpg', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])]),
            preserve_default=b'I01\n',
        ),
    ]
