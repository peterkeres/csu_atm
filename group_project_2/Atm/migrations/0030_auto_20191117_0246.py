# Generated by Django 2.2.6 on 2019-11-17 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Atm', '0029_auto_20191117_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view_atm_status',
            name='ATM_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='Atm.ATM'),
        ),
    ]
