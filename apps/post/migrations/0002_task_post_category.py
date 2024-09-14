# Generated by Django 5.1.1 on 2024-09-14 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок задачи ')),
                ('description', models.TextField(verbose_name='Описание для задачи')),
                ('completed', models.BooleanField(blank=True, default=False, null=True, verbose_name='ВЫполнено')),
                ('created', models.DateTimeField(verbose_name='Дата создания')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_post', to='categories.category'),
        ),
    ]