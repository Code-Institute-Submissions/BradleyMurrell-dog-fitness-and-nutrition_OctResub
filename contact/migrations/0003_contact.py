# Generated by Django 3.2.15 on 2022-09-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0002_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('dogs_name', models.CharField(max_length=50)),
                ('dogs_age', models.CharField(max_length=50)),
                ('dogs_breed', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=2000)),
            ],
        ),
    ]
