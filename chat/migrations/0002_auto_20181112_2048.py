# Generated by Django 2.1 on 2018-11-13 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='tel',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='whatsUp',
        ),
    ]