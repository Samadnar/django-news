# Generated by Django 4.2.7 on 2023-11-12 08:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]