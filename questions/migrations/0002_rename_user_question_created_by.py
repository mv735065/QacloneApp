# Generated by Django 5.0.7 on 2024-07-23 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='user',
            new_name='created_by',
        ),
    ]
