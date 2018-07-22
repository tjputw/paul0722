# Generated by Django 2.0 on 2018-07-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happy', '0015_healthy_ptime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=1000)),
                ('vote', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=20)),
                ('contenthref', models.CharField(max_length=50)),
                ('img', models.CharField(default='Null', max_length=200)),
                ('headpic', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'smile',
            },
        ),
    ]
