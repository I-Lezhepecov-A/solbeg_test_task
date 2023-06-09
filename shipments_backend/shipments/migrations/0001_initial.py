# Generated by Django 4.2.1 on 2023-06-03 12:53

import django.db.models.deletion
from django.db import migrations, models

import shipments.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('direction', '0001_initial'),
        ('transporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=shipments.models.code_gen, max_length=32)),
                ('arival_date', models.DateTimeField()),
                ('overdue', models.BooleanField(default=False)),
                ('sent_date', models.DateTimeField()),
                ('is_arrived', models.BooleanField(default=False)),
                ('to_direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direction.direction')),
                ('transporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='transporter.transporter')),
            ],
        ),
    ]
