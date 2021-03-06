# Generated by Django 3.1.1 on 2020-10-31 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20201031_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='document',
            field=models.FileField(blank=True, upload_to='clubs/documents'),
        ),
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(blank=True, upload_to='clubs/images'),
        ),
        migrations.AlterField(
            model_name='group',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
