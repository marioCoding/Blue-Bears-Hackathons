# Generated by Django 4.1.2 on 2022-10-23 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UniLinkedApp', '0002_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='user',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='user',
            new_name='username',
        ),
    ]
