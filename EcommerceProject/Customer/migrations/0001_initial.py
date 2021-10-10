# Generated by Django 3.2.7 on 2021-10-07 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Seller', '0003_alter_mobile_warranty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.customer')),
                ('grocery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Seller.grocery')),
                ('laptop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Seller.laptop')),
                ('mobile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Seller.mobile')),
            ],
        ),
    ]
