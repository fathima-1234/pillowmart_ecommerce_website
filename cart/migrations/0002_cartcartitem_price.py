# Generated by Django 4.2 on 2023-04-25 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartcartitem',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]