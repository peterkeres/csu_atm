# Generated by Django 2.2.6 on 2019-11-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atm', '0020_remove_view_atm_status_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='view_atm_status',
            name='balance',
            field=models.CharField(default='0', max_length=20),
        ),
    ]