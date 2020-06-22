# Generated by Django 2.2.1 on 2019-09-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=255)),
                ('feedID', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=255)),
                ('number_of_post', models.IntegerField(default=0)),
                ('followers', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('full_text', models.CharField(max_length=8191)),
                ('crawled_dt', models.DateTimeField()),
                ('post_dt', models.DateTimeField()),
                ('author_name', models.CharField(max_length=255)),
                ('like', models.IntegerField(default=0)),
                ('comment', models.IntegerField(default=0)),
            ],
        ),
    ]
