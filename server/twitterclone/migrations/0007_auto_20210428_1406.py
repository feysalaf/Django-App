# Generated by Django 3.2 on 2021-04-28 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0006_auto_20210428_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='following',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterclone.user'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterclone.user'),
        ),
    ]
