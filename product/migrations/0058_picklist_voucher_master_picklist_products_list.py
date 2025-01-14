# Generated by Django 4.2.5 on 2025-01-14 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0057_alter_sales_voucher_finish_goods_unique_serial_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picklist_voucher_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picklist_no', models.CharField(max_length=100, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('c_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Picklist_products_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.BigIntegerField()),
                ('bin_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.finished_product_warehouse_bin')),
                ('picklist_master_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picklist_products_list', to='product.picklist_voucher_master')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.pproduct_creation')),
            ],
        ),
    ]
