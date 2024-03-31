# Generated by Django 5.0.2 on 2024-03-28 09:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('learningapp', '0002_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedCourse',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='completed', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('quantity', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningapp.courseproduct')),
            ],
        ),
    ]
