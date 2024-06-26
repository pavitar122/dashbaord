# Generated by Django 5.0.3 on 2024-03-20 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_system', '0002_alter_doctor_profile_picture_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/images/blog_images/')),
                ('category', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('content', models.TextField()),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('is_draft', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='profile_picture',
            field=models.ImageField(upload_to='static/images/Doctor/'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profile_picture',
            field=models.ImageField(upload_to='static/images/Patient/'),
        ),
    ]
