# Generated by Django 5.1.1 on 2024-10-05 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('programming_language', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='user_image/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
