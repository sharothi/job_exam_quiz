# Generated by Django 4.1.3 on 2022-11-04 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_alter_student_institution_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='by_agent',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='institution_info',
        ),
        migrations.RemoveField(
            model_name='examinationinfo',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='examinationinfo',
            name='institution_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='institution_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='institution_name',
        ),
        migrations.DeleteModel(
            name='Agent',
        ),
        migrations.DeleteModel(
            name='Institution',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]