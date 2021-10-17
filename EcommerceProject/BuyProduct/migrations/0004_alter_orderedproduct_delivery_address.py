# Generated by Django 3.2.7 on 2021-10-16 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
        ('BuyProduct', '0003_alter_orderedproduct_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedproduct',
            name='delivery_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.addresses'),
        ),
    ]