# Generated by Django 3.2 on 2021-04-29 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0010_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='following',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterclone.profile'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterclone.profile'),
        ),
    ]