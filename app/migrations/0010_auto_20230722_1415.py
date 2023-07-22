# Generated by Django 3.2.20 on 2023-07-22 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=59, verbose_name='タグ')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='_app_post_tag_+', to='app.Post', verbose_name='関連'),
        ),
    ]
