# Generated by Django 4.0 on 2023-02-04 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
        ('teacher', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='teacher',
            field=models.ManyToManyField(blank=True, related_name='teacher_semester', to='teacher.Teacher'),
        ),
        migrations.AddField(
            model_name='revenue',
            name='students',
            field=models.ManyToManyField(related_name='student', to='student.Student'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject_for_lesson',
            field=models.ManyToManyField(related_name='subject_lesson', to='school.Subject'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_lesson', to='teacher.teacher'),
        ),
        migrations.AddField(
            model_name='batch',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.academicsession'),
        ),
        migrations.AddField(
            model_name='awards',
            name='owner_awards_account',
            field=models.ManyToManyField(related_name='awards_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='batch',
            unique_together={('year', 'number')},
        ),
    ]
