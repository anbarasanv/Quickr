# Generated by Django 2.2.1 on 2019-05-21 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
