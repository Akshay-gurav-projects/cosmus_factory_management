# Generated by Django 4.2.5 on 2024-11-14 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_remove_raw_material_production_total_stock_in_cutting_stage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='raw_material_production_total',
            name='stock_in_cutting_stage',
            field=models.DecimalField(decimal_places=3, default=23, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='raw_material_production_total',
            name='stock_in_labour_workout_stage',
            field=models.DecimalField(decimal_places=3, default=23, max_digits=10),
            preserve_default=False,
        ),
    ]
