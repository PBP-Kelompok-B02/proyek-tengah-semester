# Generated by Django 5.1.2 on 2024-10-27 02:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_bookmark_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
