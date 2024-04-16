# Generated by Django 4.2.7 on 2024-03-29 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_image_product_primary_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.CharField(choices=[('★', 1), ('★★', 2), ('★★★', 3), ('★★★★', 4), ('★★★★★', 5)], default=None, max_length=5),
        ),
    ]