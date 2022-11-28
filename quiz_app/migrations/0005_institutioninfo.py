# Generated by Django 4.1.3 on 2022-11-17 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0004_alter_teacher_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_header', models.CharField(max_length=200, null=True)),
                ('homepage_message', models.CharField(max_length=700, null=True)),
                ('activation_message', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]