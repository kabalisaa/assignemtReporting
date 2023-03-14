# Generated by Django 4.1.7 on 2023-03-14 06:44

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
            name="Assignment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, unique=True)),
                (
                    "task_file",
                    models.FileField(max_length=255, upload_to="static/assignment/"),
                ),
                ("created_date", models.DateField(auto_now=True)),
                ("due_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="AssignmentReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "student_report",
                    models.FileField(upload_to="static/assignment/report/"),
                ),
                ("submited_date", models.DateField(auto_now=True)),
                (
                    "assignmet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="training.assignment",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClassRoom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("class_name", models.CharField(max_length=255, unique=True)),
                ("created_date", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("module_name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Topics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("topic_title", models.CharField(max_length=255, unique=True)),
                ("content", models.TextField()),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="training.module",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OngoingModule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("startPeriod_date", models.DateField()),
                ("endPeriod_date", models.DateField()),
                (
                    "class_room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="training.classroom",
                    ),
                ),
                (
                    "instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="training.module",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AssignmentReportComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.TextField()),
                ("created_date", models.DateField(auto_now=True)),
                (
                    "assignment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="training.assignmentreport",
                    ),
                ),
                (
                    "instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="assignment",
            name="on_module",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="training.ongoingmodule"
            ),
        ),
    ]
