# Generated by Django 4.2.7 on 2024-03-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_productreview_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colour',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discreption',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='fretboard',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='frets',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='hardware',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='mastertone',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='mastervol',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='neck',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pickups',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='scale',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='strings',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='switches',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='trem',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tuners',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='wood',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(blank=True),
        ),
    ]