# Generated by Django 5.0.1 on 2024-01-27 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_alter_article_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subarticle',
            name='image',
        ),
        migrations.RemoveField(
            model_name='subarticle',
            name='title',
        ),
    ]
