# Generated by Django 4.2 on 2023-04-16 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_expired_quantity_remove_outgoing_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='expired',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]