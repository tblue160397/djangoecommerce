# Generated by Django 3.1.7 on 2021-04-07 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_payment_pay_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='dob',
            field=models.DateTimeField(null=True),
        ),
    ]
