# Generated by Django 3.1.7 on 2021-04-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('just_co_away', '0009_auto_20210425_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='address',
            field=models.CharField(default='N/A', max_length=400),
        ),
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='pincode',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.CharField(default='N/A', max_length=500),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='verified_on',
            field=models.CharField(default='N/A', max_length=200),
        ),
    ]
