from django.db import models
from apps.categories.models import Category
# Create your models here.
class Post(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name= 'category_post',
        blank=True, null=True
        )
    title = models.CharField(
        max_length=255,
        verbose_name='Название товара'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='post_image/',
        verbose_name='Фото товара'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'

