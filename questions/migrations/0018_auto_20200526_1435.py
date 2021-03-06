# Generated by Django 3.0.5 on 2020-05-26 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0017_auto_20200526_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='answers',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='answer', to='questions.Answer', verbose_name='Ответы'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='current_user',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='question_in_block',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_in_block', to='questions.QuestionInBlock'),
        ),
    ]
