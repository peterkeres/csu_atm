# Generated by Django 2.2.6 on 2019-11-16 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atm', '0022_remove_atm_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view_atm_status',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]