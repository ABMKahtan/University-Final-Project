# Generated by Django 3.2.4 on 2021-06-08 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='item',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='price_Per_Unit_Sell',
        ),
    ]
