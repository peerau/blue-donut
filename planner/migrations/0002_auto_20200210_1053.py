# Generated by Django 3.0.3 on 2020-02-10 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='popularsystems',
            old_name='system_name',
            new_name='popular',
        ),
    ]
