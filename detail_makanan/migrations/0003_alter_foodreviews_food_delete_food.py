# Generated by Django 5.1.2 on 2024-10-25 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail_makanan', '0002_alter_foodreviews_image_url'),
        ('main', '0004_alter_food_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodreviews',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.food'),
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]