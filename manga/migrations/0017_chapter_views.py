# Generated by Django 3.0.3 on 2021-03-04 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0016_auto_20210303_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
