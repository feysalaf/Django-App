# Generated by Django 3.2 on 2021-04-28 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0009_auto_20210428_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('user_name', models.CharField(max_length=200)),
            ],
        ),
    ]
