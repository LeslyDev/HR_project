# Generated by Django 3.0.5 on 2020-06-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0028_auto_20200603_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_passed',
            field=models.BooleanField(default=False),
        ),
    ]
