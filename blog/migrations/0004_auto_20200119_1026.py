# Generated by Django 2.2.9 on 2020-01-19 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200119_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='category_id',
            new_name='category',
        ),
    ]
