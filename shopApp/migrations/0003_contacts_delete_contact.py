# Generated by Django 4.2.19 on 2025-03-18 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_full_name', models.CharField(max_length=100, unique=True)),
                ('contact_address', models.CharField(max_length=250)),
                ('contact_phone', models.CharField(max_length=30)),
                ('contact_email', models.CharField(max_length=50)),
                ('contact_active', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
