# Generated by Django 4.1.3 on 2022-11-04 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_remove_institution_by_agent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]