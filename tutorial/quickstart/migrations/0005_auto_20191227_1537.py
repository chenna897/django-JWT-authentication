# Generated by Django 2.0.13 on 2019-12-27 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_projects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
        migrations.AlterModelTable(
            name='project',
            table='project',
        ),
    ]