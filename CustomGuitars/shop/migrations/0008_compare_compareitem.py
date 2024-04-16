# Generated by Django 4.2.7 on 2024-03-25 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_colour_product_discreption_product_fretboard_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compare_id', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'db_table': 'Compare',
            },
        ),
        migrations.CreateModel(
            name='CompareItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('compare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.compare')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'db_table': 'CompareItem',
            },
        ),
    ]