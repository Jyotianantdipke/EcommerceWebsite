# Generated by Django 3.2.7 on 2021-10-07 06:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0006_alter_customerprofile_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='Mobile_no',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1000000000, 'The Mobile number must contains 10 digits only.'), django.core.validators.MaxValueValidator(9999999999, 'The Mobile number must contains 10 digits only.')]),
        ),
    ]
