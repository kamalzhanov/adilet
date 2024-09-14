from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок задачи '
    )
    description = models.TextField(
        verbose_name='Описание для задачи'
    )
    completed = models.BooleanField(
        default= False, verbose_name='Вsполнено',
        blank= True, null= True 
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add= True
    )
    
    def __str__ (self):
        return self.title
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
