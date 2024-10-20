# Generated by Django 5.1.2 on 2024-10-20 09:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=0, max_digits=6)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('restaurant', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('open_time', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
