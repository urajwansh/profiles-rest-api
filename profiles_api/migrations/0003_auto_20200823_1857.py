# Generated by Django 2.2 on 2020-08-23 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='status_text',
            new_name='statustext',
        ),
    ]
