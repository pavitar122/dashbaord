# Generated by Django 5.0.3 on 2024-03-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_system', '0004_rename_first_name_blogpost_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]