# Generated by Django 4.2.7 on 2023-11-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_news_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='view_count',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
