# Generated by Django 2.2 on 2019-04-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190419_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
