# Generated by Django 5.0.1 on 2024-01-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customiser',
            field=models.BooleanField(default=False),
        ),
    ]