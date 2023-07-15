# Generated by Django 3.2.20 on 2023-07-15 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230715_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sakusya',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=70000),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
