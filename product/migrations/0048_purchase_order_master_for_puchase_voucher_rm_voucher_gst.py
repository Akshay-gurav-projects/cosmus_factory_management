# Generated by Django 4.2.5 on 2024-12-21 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0047_alter_finishedgoodsbinallocation_related_purchase_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_order_master_for_puchase_voucher_rm',
            name='voucher_gst',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
    ]
