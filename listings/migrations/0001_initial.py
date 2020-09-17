# Generated by Django 3.0.8 on 2020-08-16 06:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('size', models.IntegerField()),
                ('bathroom', models.DecimalField(decimal_places=1, max_digits=2)),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('garage', models.IntegerField()),
                ('main_image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('aux_image_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('aux_image_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('aux_image_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('aux_image_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('aux_image_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('listing_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
    ]
