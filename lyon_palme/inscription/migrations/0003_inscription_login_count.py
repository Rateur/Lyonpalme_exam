# Generated by Django 4.1.4 on 2023-06-08 08:38

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0002_inscription_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='login_count',
            field=django_cryptography.fields.encrypt(models.IntegerField(null=True)),
        ),
    ]
