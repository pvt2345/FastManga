# Generated by Django 3.0.3 on 2021-02-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0005_auto_20210228_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='code',
            field=models.CharField(max_length=30),
        ),
    ]