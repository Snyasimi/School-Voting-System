# Generated by Django 4.1.4 on 2023-04-25 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voters',
            old_name='Id',
            new_name='User_id',
        ),
    ]
