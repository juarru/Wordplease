# Generated by Django 2.0.1 on 2018-01-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blogging.Category'),
        ),
    ]
