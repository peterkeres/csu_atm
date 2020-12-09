# Generated by Django 2.2.6 on 2019-11-17 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Atm', '0028_auto_20191116_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_new_atm_card',
            name='account_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Atm.Account_Extension'),
        ),
        migrations.AlterField(
            model_name='view_atm_status',
            name='ATM_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='Atm.ATM', unique=True),
        ),
    ]