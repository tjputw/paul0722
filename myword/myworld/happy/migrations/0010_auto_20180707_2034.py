# Generated by Django 2.0 on 2018-07-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happy', '0009_auto_20180707_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmdown',
            name='movie_download_url',
            field=models.CharField(max_length=1000),
        ),
    ]