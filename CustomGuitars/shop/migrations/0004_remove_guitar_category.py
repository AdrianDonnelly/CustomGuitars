# Generated by Django 5.0.1 on 2024-01-28 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_product_customiser_guitar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guitar',
            name='category',
        ),
    ]