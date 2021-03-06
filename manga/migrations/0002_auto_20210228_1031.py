# Generated by Django 3.0.3 on 2021-02-28 03:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='manga',
            name='code',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manga',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='manga',
            name='ongoing',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='manga',
            name='total_star',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='manga',
            name='total_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='manga',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='manga',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdn_url', models.CharField(max_length=200)),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.Manga')),
            ],
        ),
        migrations.AddField(
            model_name='manga',
            name='author',
            field=models.ManyToManyField(to='manga.Author'),
        ),
        migrations.AddField(
            model_name='manga',
            name='genre',
            field=models.ManyToManyField(to='manga.Genre'),
        ),
    ]
