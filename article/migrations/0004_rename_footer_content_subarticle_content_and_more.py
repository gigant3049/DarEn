# Generated by Django 5.0.1 on 2024-01-26 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_created_date_subarticle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subarticle',
            old_name='footer_content',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='subarticle',
            name='header_content',
        ),
    ]
