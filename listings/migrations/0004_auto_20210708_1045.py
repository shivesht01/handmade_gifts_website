# Generated by Django 3.0.8 on 2021-07-08 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20210706_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='aux_video',
            field=models.FileField(null=True, upload_to='videos/', verbose_name='Video_if_any'),
        ),
    ]
