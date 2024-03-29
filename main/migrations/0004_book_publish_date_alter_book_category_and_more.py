# Generated by Django 5.0.1 on 2024-01-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_book_description_book_edition_book_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=900, null=True),
        ),
    ]
