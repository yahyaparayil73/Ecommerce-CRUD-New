# Generated by Django 4.1.7 on 2023-03-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50)),
                ('c_email', models.CharField(max_length=50)),
                ('c_address', models.CharField(max_length=100)),
                ('c_phone_number', models.BigIntegerField()),
                ('c_gender', models.CharField(max_length=10)),
            ],
        ),
    ]