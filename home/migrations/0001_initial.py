# Generated by Django 3.2.7 on 2021-10-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(default='', max_length=50)),
                ('roll_num', models.BigIntegerField()),
                ('password', models.CharField(default='', max_length=70)),
            ],
        ),
    ]
