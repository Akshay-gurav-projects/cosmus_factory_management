# Generated by Django 4.2.5 on 2024-12-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0050_product_purchase_voucher_master_narration'),
    ]

    operations = [
        migrations.AddField(
            model_name='finished_goods_stock_transfermaster',
            name='narration',
            field=models.CharField(default='No narration', max_length=255),
            preserve_default=False,
        ),
    ]
