# Generated by Django 3.2.7 on 2021-10-07 06:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_auto_20211007_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='Mobile_no',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(999999999)]),
        ),
    ]