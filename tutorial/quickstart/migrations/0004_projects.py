# Generated by Django 2.0.13 on 2019-12-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20191226_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'projects',
            },
        ),
    ]