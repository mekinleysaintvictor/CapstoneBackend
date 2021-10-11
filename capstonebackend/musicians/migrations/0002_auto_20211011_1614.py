# Generated by Django 3.2.8 on 2021-10-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='jam',
        ),
        migrations.RemoveField(
            model_name='musician',
            name='profilePic',
        ),
        migrations.RemoveField(
            model_name='musician',
            name='video',
        ),
        migrations.AddField(
            model_name='musician',
            name='genres',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='musician',
            name='influences',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='musician',
            name='instruments',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='musician',
            name='aboutMe',
            field=models.CharField(default='None', max_length=500),
        ),
    ]
