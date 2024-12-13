# Generated by Django 4.2.5 on 2024-11-09 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_remove_labour_work_in_product_to_item_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='raw_material_product_ref_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_product_qty', models.IntegerField(default=0)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='raw_material_production_estimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_material_godown_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.godown_raw_material')),
            ],
        ),
        migrations.CreateModel(
            name='raw_material_production_total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('total_consump', models.DecimalField(decimal_places=3, max_digits=10)),
                ('godown_stock', models.DecimalField(decimal_places=3, max_digits=10)),
                ('balance_stock', models.DecimalField(decimal_places=3, max_digits=10)),
                ('raw_material_estination_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.raw_material_production_estimation')),
            ],
        ),
        migrations.CreateModel(
            name='raw_material_product_wise_qty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_sku', models.CharField(max_length=100)),
                ('product_color', models.CharField(max_length=100)),
                ('estimate_qty', models.IntegerField(default=0)),
                ('raw_material_ref_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.raw_material_product_ref_items')),
            ],
        ),
        migrations.CreateModel(
            name='raw_material_product_to_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_sku', models.CharField(max_length=50)),
                ('product_color', models.CharField(max_length=60)),
                ('material_name', models.CharField(max_length=60)),
                ('rate', models.DecimalField(decimal_places=3, max_digits=10)),
                ('panha', models.DecimalField(decimal_places=3, max_digits=10)),
                ('units', models.DecimalField(decimal_places=3, max_digits=10)),
                ('unit_value', models.CharField(max_length=100)),
                ('g_total', models.DecimalField(decimal_places=3, max_digits=10)),
                ('g_total_combi', models.DecimalField(decimal_places=3, max_digits=10)),
                ('consumption', models.DecimalField(decimal_places=3, max_digits=10)),
                ('combi_consumption', models.DecimalField(decimal_places=3, max_digits=10)),
                ('total_comsumption', models.DecimalField(decimal_places=3, max_digits=10)),
                ('physical_stock', models.DecimalField(decimal_places=3, max_digits=10)),
                ('balance_physical_stock', models.DecimalField(decimal_places=3, max_digits=10)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('Remark', models.CharField(max_length=50)),
                ('pcs', models.IntegerField(default=0)),
                ('raw_material_ref_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.raw_material_product_ref_items')),
            ],
        ),
        migrations.AddField(
            model_name='raw_material_product_ref_items',
            name='raw_material_estination_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.raw_material_production_estimation'),
        ),
    ]
