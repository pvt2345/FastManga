# Generated by Django 3.0.3 on 2021-02-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0010_auto_20210228_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='chapter_code',
        ),
        migrations.AddField(
            model_name='chapter',
            name='code',
            field=models.CharField(default=None, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='manga',
            name='code',
            field=models.CharField(default='0000', max_length=30, unique=True),
        ),
    ]
