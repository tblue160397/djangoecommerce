# Generated by Django 3.1.7 on 2021-03-30 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210329_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
