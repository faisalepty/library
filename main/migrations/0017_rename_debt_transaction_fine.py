# Generated by Django 5.0.1 on 2024-01-26 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_transaction_copyid_transaction_debt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='debt',
            new_name='fine',
        ),
    ]
