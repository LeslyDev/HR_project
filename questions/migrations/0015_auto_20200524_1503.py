# Generated by Django 3.0.5 on 2020-05-24 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_auto_20200524_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='answers',
            field=models.ManyToManyField(default='', related_name='answer', to='questions.Answer', verbose_name='Ответы'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='question_in_block',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='question_in_block', to='questions.QuestionInBlock'),
        ),
    ]
