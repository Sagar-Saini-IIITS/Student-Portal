# Generated by Django 3.1.1 on 2020-12-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fee', '0010_auto_20201205_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeupdate',
            name='payment_status',
            field=models.CharField(default=0, max_length=10000000),
        ),
        migrations.AddField(
            model_name='feeupdate',
            name='transaction_id',
            field=models.CharField(default=0, max_length=10000000),
        ),
        migrations.AlterField(
            model_name='feeupdate',
            name='amount',
            field=models.CharField(default=0, max_length=10000000),
        ),
        migrations.AlterField(
            model_name='feeupdate',
            name='payment_id',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
