# Generated by Django 3.0.5 on 2020-07-25 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_leads'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='lead_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 25, 13, 7, 8, 696155)),
        ),
        migrations.AlterField(
            model_name='leads',
            name='lead_converted',
            field=models.IntegerField(default=3),
        ),
    ]
