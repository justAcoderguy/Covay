# Generated by Django 3.1.7 on 2021-04-25 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('just_co_away', '0006_auto_20210425_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='landline_number',
            field=models.CharField(default='N/A', max_length=300),
        ),
        migrations.AddField(
            model_name='listing',
            name='whatsapp_number',
            field=models.CharField(default='N/A', max_length=300),
        ),
        migrations.AlterField(
            model_name='listing',
            name='maximum_delivery_distance',
            field=models.CharField(default='N/A', max_length=300),
        ),
        migrations.AlterField(
            model_name='listing',
            name='phone_number',
            field=models.CharField(default='N/A', max_length=300),
        ),
    ]
