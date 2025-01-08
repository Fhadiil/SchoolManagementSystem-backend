# Generated by Django 5.1.3 on 2025-01-08 22:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualifications', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=15)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='teachers/photos/')),
                ('assigned_classes', models.ManyToManyField(blank=True, related_name='teachers', to='classes.class')),
                ('subjects', models.ManyToManyField(related_name='teachers', to='teachers.subject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
