# Generated by Django 2.2.6 on 2019-11-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atm', '0012_auto_20191112_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='ATM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
