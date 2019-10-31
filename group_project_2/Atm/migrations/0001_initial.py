# Generated by Django 2.2.6 on 2019-10-31 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_Extension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15)),
                ('balance', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
    ]
