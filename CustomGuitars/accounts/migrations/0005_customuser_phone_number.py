# Generated by Django 4.2.7 on 2024-03-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_secret_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.BigIntegerField(null=True),
        ),
    ]
