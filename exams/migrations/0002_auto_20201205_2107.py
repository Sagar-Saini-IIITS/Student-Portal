# Generated by Django 3.1.1 on 2020-12-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='roll_number',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='examination',
            name='sub1_marks',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='examination',
            name='sub2_marks',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='examination',
            name='sub3_marks',
            field=models.IntegerField(default=''),
        ),
    ]