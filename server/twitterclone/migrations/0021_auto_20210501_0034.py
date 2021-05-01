# Generated by Django 3.2 on 2021-05-01 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0020_auto_20210501_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollowing',
            name='following_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='twitterclone.profile'),
        ),
        migrations.AlterField(
            model_name='userfollowing',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='twitterclone.profile'),
        ),
    ]
