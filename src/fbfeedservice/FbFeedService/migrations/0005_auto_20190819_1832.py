# Generated by Django 2.2.1 on 2019-08-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FbFeedService', '0004_update_feed_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='crawled_dt',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='feed',
            name='post_dt',
            field=models.DateTimeField(),
        ),
    ]
