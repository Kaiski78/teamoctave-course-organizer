# Generated by Django 4.1.2 on 2022-12-01 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('number', 'department')},
        ),
    ]
