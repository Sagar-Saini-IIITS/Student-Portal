# Generated by Django 3.1.1 on 2020-10-31 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0008_cnotice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cnotice',
            old_name='desc',
            new_name='descp',
        ),
        migrations.RemoveField(
            model_name='group',
            name='category',
        ),
    ]
