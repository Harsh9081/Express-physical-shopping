# Generated by Django 4.0.1 on 2022-04-18 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin2', '0004_rename_profile2_profile_alter_profile_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='forget_password_token',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
