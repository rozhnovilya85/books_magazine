from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок') # заголовок поста
    content = models.TextField(max_length=10000, verbose_name='Текст поста') # текст поста
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    date_update = models.DateField(auto_now=True, null=True, verbose_name='Дата изменения записи')

    def __str__(self):  # Переопределение названия объекта
        return self.title

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Пост'  # Надпись в единственном числе
        verbose_name_plural = 'Посты'  # Надпись во множественном числе
        ordering = ['date_create']  # Сортировка полей (по возрастанию)