# Generated by Django 2.2.7 on 2019-11-24 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0009_clothing_itemid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='itemid',
            field=models.CharField(max_length=120),
        ),
    ]