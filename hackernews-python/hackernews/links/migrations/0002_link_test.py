# Generated by Django 2.1.4 on 2021-05-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='test',
            field=models.TextField(blank=True),
        ),
    ]
