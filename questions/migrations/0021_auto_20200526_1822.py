# Generated by Django 3.0.5 on 2020-05-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0020_auto_20200526_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='block',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='question',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='question',
            field=models.ManyToManyField(blank=True, default='', related_name='user_question', to='questions.Question', verbose_name='Вопросы'),
        ),
    ]
