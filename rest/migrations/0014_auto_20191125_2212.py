# Generated by Django 2.2.7 on 2019-11-25 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0013_auto_20191125_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothing',
            name='image2',
            field=models.FileField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='clothing',
            name='image3',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]