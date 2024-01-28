# Generated by Django 5.0.1 on 2024-01-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_book_id_transaction_book_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='copyId',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='debt',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]