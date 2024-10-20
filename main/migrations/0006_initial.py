# Generated by Django 5.1.2 on 2024-10-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0005_delete_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
