# Generated by Django 3.1.1 on 2020-12-05 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fee', '0007_auto_20201205_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feesem',
            old_name='item_amount',
            new_name='pay_amount',
        ),
        migrations.RenameField(
            model_name='feesem',
            old_name='sem',
            new_name='typee',
        ),
    ]