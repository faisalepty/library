# Generated by Django 5.0.1 on 2024-01-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_member_national_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='national_id',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
