from operator import mod
from turtle import title
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='название поста')
    content = models.TextField(verbose_name='текст для поста')
    publish = models.BooleanField(default=True)
    datearticle = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новая статья'
        verbose_name_plural = 'Все посты'

    def __str__(self):
        return self.title
