from django.db import models
from django.urls import reverse

# Create your models here.


'''
Category
==========
title, slug

Tag
==========
title, slug

Post
==========
title, slug, author, content, created_at, photo, views, category, tags
'''


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    # Метод, который поможет нам сформировывать корректные ссылки
    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        # Название модели в админке
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        # Название модели в админке
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    # Метод, который поможет нам сформировывать корректные ссылки
    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models. TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Тэг')

    def __str__(self):
        return self.title

    # Метод, который поможет нам сформировывать корректные ссылки
    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created_at']
        # Название модели в админке
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'

