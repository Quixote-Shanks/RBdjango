# Generated by Django 4.2.1 on 2023-05-25 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_lecturer_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='courses',
        ),
    ]