# Generated by Django 2.2.7 on 2019-11-25 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0014_auto_20191125_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='desc',
            field=models.TextField(max_length=255),
        ),
    ]
