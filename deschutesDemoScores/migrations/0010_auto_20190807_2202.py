# Generated by Django 2.2 on 2019-08-07 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deschutesDemoScores', '0009_score_division'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='division',
        ),
        migrations.AddField(
            model_name='team',
            name='division',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='deschutesDemoScores.Division'),
            preserve_default=False,
        ),
    ]
