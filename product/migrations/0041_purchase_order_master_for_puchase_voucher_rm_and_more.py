# Generated by Django 4.2.5 on 2024-12-09 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0040_sales_voucher_master_finish_goods_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchase_order_master_for_puchase_voucher_rm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_no', models.IntegerField(unique=True)),
                ('party_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='purchase_order_for_puchase_voucher_rm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.item_creation')),
            ],
        ),
    ]
