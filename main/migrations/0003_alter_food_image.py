# Generated by Django 5.1.2 on 2024-10-26 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_food_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.TextField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.its.ac.id%2Ftmesin%2Ffasilitas%2Flaboratorium-2%2Fno-image%2F&psig=AOvVaw3MxCmHHuz26CagUzVTBH79&ust=1729935269596000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMiWpJudqYkDFQAAAAAdAAAAABAJ'),
        ),
    ]