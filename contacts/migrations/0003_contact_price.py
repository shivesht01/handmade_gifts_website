# Generated by Django 3.0.8 on 2021-07-08 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20210708_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='price',
            field=models.TextField(default=0),
        ),
    ]