# Generated by Django 2.0 on 2018-07-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happy', '0003_auto_20180706_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musiclist',
            name='listen_num',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='musiclist',
            name='song_user',
            field=models.CharField(max_length=100),
        ),
    ]
