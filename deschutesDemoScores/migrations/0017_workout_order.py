# Generated by Django 2.2 on 2020-02-04 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deschutesDemoScores', '0016_auto_20191029_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
