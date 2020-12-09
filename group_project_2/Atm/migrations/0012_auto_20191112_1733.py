# Generated by Django 2.2.6 on 2019-11-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atm', '0011_auto_20191111_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view_atm_status',
            name='id',
        ),
        migrations.AlterField(
            model_name='view_atm_status',
            name='ATM_address',
            field=models.CharField(default='', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='view_atm_status',
            name='ATM_status',
            field=models.CharField(choices=[('Active', 'Active'), ('Down', 'Down')], default='Down', max_length=10),
        ),
    ]