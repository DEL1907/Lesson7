from django.db import models


class Recipes(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    ingredients = models.TextField(max_length=500, verbose_name='Ингредиенты')
    description = models.TextField(max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
