# Generated by Django 4.2.7 on 2023-11-08 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
    ]