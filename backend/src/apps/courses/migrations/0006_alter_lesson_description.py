# Generated by Django 5.1.4 on 2024-12-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_lesson_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(max_length=512),
        ),
    ]
