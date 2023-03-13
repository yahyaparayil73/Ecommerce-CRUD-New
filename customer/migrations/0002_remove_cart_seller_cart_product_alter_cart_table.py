# Generated by Django 4.1.7 on 2023-03-13 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='seller',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller.product'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
    ]
