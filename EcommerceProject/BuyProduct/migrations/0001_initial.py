# Generated by Django 3.2.7 on 2021-10-16 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '__first__'),
        ('Seller', '__first__'),
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('payment_mode', models.CharField(choices=[('Online', 'Online'), ('Cash on Delivery', 'Cash on Delivery')], max_length=16)),
                ('order_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.customer')),
                ('delivery_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Customer.addresses')),
                ('grocery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Seller.grocery')),
                ('laptop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Seller.laptop')),
                ('mobile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Seller.mobile')),
            ],
        ),
    ]
