# Generated by Django 3.1.1 on 2020-11-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lfitems', '0002_auto_20201102_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lf',
            name='item_document',
            field=models.FileField(blank=True, null=True, upload_to='lfitems/lostfound'),
        ),
        migrations.AlterField(
            model_name='lf',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='lfitems/lostfound'),
        ),
    ]
