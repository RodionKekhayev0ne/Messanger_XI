# Generated by Django 5.0.4 on 2024-04-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.CharField(default='', max_length=250),
        ),
    ]
