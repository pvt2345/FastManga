# Generated by Django 3.0.3 on 2021-02-28 09:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0014_auto_20210228_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
