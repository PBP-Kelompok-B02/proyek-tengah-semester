# Generated by Django 5.1.2 on 2024-10-25 09:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='rating',
        ),
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.its.ac.id%2Ftmesin%2Ffasilitas%2Flaboratorium-2%2Fno-image%2F&psig=AOvVaw3MxCmHHuz26CagUzVTBH79&ust=1729935269596000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMiWpJudqYkDFQAAAAAdAAAAABAJ', max_length=255),
        ),
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
