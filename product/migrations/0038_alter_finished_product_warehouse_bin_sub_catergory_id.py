# Generated by Django 4.2.5 on 2024-12-02 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_alter_product_2_item_through_table_pproduct_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finished_product_warehouse_bin',
            name='sub_catergory_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sub_categories', to='product.subcategory'),
        ),
    ]
