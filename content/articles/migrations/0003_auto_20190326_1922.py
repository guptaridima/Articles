# Generated by Django 2.1.7 on 2019-03-26 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_content'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='article',
            unique_together={('title', 'author_name')},
        ),
    ]
