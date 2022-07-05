# Generated by Django 2.1 on 2018-11-12 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField(default=0, verbose_name='age')),
                ('email', models.EmailField(max_length=30)),
                ('tel', models.CharField(max_length=11)),
                ('whatsUp', models.CharField(max_length=42)),
                ('picture', models.ImageField(blank=True, default='portrait/default.png', upload_to='portrait')),
                ('follower', models.ManyToManyField(related_name='followed', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
