# Generated by Django 3.0.5 on 2020-05-26 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_auto_20200526_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='block',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_block', to='questions.Block', verbose_name='Блок'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='question',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_question', to='questions.Question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='answers',
            field=models.ManyToManyField(blank=True, default='', related_name='answer', to='questions.Answer', verbose_name='Ответы'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_user',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Пользователь'),
        ),
    ]
