# Generated by Django 4.2.2 on 2023-07-09 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='Price',
            new_name='customer_fee',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='Name',
        ),
    ]