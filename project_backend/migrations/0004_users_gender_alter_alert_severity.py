# Generated by Django 4.1 on 2024-05-28 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_backend', '0003_alter_users_options_alter_users_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='severity',
            field=models.CharField(choices=[('normal', 'normal'), ('severe', 'severe'), ('critical', 'critical')], max_length=20),
        ),
    ]