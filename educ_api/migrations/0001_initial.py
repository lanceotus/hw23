# Generated by Django 2.2.2 on 2019-06-20 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('students', models.ManyToManyField(blank=True, related_name='courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-', max_length=255)),
                ('surname', models.CharField(default='-', max_length=255)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='educ_api.Course')),
            ],
            options={
                'ordering': ['time'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='tutors',
            field=models.ManyToManyField(blank=True, related_name='courses', to='educ_api.Tutor'),
        ),
    ]
