# Generated by Django 2.2.6 on 2019-11-17 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atm', '0007_auto_20191117_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='date',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]