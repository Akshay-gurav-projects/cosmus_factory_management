# Generated by Django 4.2.5 on 2024-12-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0042_purchase_order_for_puchase_voucher_rm_master_instance'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_order_master_for_puchase_voucher_rm',
            name='payment_term',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
