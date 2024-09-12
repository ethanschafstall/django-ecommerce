# Generated by Django 2.2.28 on 2024-09-12 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('account_creation_date', models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 12, 9, 53, 23, 498428))),
            ],
        ),
    ]
