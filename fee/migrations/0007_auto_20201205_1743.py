# Generated by Django 3.1.1 on 2020-12-05 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fee', '0006_auto_20201205_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feesem',
            old_name='amount',
            new_name='item_amount',
        ),
    ]
