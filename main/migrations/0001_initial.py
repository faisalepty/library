# Generated by Django 5.0.1 on 2024-01-13 01:13

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('fee', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=200)),
                ('debt', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('issue_date', models.DateTimeField()),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.member')),
            ],
        ),
    ]
