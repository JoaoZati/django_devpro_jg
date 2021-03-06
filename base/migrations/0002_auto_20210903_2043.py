# Generated by Django 3.2.7 on 2021-09-03 23:43

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = {
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', base.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has '
                                                               'all permissions without explicitly assigning them.',
                                      verbose_name='superuser status'),
        ),
    }
