# Generated by Django 3.2.10 on 2024-02-02 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_category_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
