# Generated by Django 2.1.7 on 2019-03-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20190326_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
