# Generated by Django 3.2.15 on 2022-12-06 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20221206_0516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userproflie',
            name='age',
        ),
        migrations.AddField(
            model_name='userproflie',
            name='memes',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
