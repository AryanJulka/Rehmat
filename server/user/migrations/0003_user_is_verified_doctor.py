# Generated by Django 4.1.7 on 2023-02-25 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_dob_user_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified_doctor',
            field=models.BooleanField(default=False),
        ),
    ]
