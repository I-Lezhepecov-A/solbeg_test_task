# Generated by Django 4.2.1 on 2023-06-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0002_rename_arival_date_shipment_estimated_arrival_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
