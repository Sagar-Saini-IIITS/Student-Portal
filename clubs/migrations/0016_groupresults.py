# Generated by Django 3.1.1 on 2020-12-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0015_auto_20201206_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupresults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_name', models.CharField(default='', max_length=50)),
                ('result_category', models.CharField(default='', max_length=50)),
                ('result_desc', models.CharField(default='', max_length=300)),
                ('result_image', models.ImageField(blank=True, null=True, upload_to='clubs/images')),
                ('result_date', models.DateTimeField(null=True)),
                ('result_document', models.FileField(blank=True, null=True, upload_to='clubs/documents')),
            ],
        ),
    ]