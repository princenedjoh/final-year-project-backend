# Generated by Django 4.1 on 2024-05-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_backend', '0004_users_gender_alter_alert_severity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='severity',
            field=models.CharField(choices=[('critical', 'critical'), ('normal', 'normal'), ('severe', 'severe')], max_length=20),
        ),
    ]
