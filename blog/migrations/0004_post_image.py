# Generated by Django 2.1.5 on 2019-04-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190216_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
