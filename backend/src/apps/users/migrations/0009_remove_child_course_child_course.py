# Generated by Django 5.1.4 on 2024-12-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_remove_course_students'),
        ('users', '0008_customuser_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='course',
        ),
        migrations.AddField(
            model_name='child',
            name='course',
            field=models.ManyToManyField(blank=True, null=True, to='courses.course'),
        ),
    ]
