# Generated by Django 5.0.1 on 2024-01-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_book_copy_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='copy_ids',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
