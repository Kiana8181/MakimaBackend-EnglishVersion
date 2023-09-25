# Generated by Django 4.1.5 on 2023-01-21 13:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('comment', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=360)),
                ('professorName', models.CharField(max_length=50)),
                ('universityName', models.CharField(max_length=50)),
                ('comments', models.ManyToManyField(blank=True, to='api.comments')),
            ],
        ),
        migrations.CreateModel(
            name='Recourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recours', models.FileField(upload_to='recourses/')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='university', max_length=10)),
                ('universityName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('logo', models.FileField(upload_to='logos/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('type', models.CharField(default='student', max_length=10)),
                ('lastName', models.CharField(max_length=50)),
                ('nationalId', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('fieldOfStudy', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('studentNumber', models.CharField(max_length=20)),
                ('university', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=50)),
                ('favoriteCourse', models.ManyToManyField(blank=True, to='api.course')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Porfessor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('type', models.CharField(default='porfessor', max_length=10)),
                ('lastName', models.CharField(max_length=50)),
                ('records', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('typeOfSpecialization', models.CharField(max_length=300)),
                ('degreeOfEducation', models.CharField(max_length=300)),
                ('university', models.CharField(max_length=50)),
                ('encyclopedia', models.FileField(upload_to='encyclopedias/')),
                ('profileImage', models.FileField(upload_to='profileImages/')),
                ('verify', models.BooleanField(default=False)),
                ('courses', models.ManyToManyField(blank=True, to='api.course')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='resourse',
            field=models.ManyToManyField(blank=True, to='api.recourses'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'course')},
                'index_together': {('user', 'course')},
            },
        ),
    ]
