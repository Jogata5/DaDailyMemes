# Generated by Django 3.2.15 on 2022-12-06 23:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20221206_2032'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProflie',
            new_name='UserProfile',
        ),
    ]
