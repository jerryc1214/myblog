# Generated by Django 2.2 on 2019-05-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0003_auto_20190529_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pic',
        ),
        migrations.AddField(
            model_name='class_name',
            name='pic',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]