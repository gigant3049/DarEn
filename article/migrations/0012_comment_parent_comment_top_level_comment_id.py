# Generated by Django 5.0.1 on 2024-02-13 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_alter_comment_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='top_level_comment_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
