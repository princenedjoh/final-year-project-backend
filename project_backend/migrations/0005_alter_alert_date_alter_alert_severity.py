# Generated by Django 4.1 on 2024-06-29 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_backend', '0004_alter_alert_severity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='alert',
            name='severity',
            field=models.CharField(choices=[('severe', 'severe'), ('critical', 'critical'), ('normal', 'normal')], max_length=20),
        ),
    ]
