from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Tag, Category
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Создаём класс формы для работы приложения ckeditor
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    # Атрибут prepopulated_fields автоматически сгенерирует нам slug на основе title
    prepopulated_fields = {"slug": ("title",)}
    # Добавляем класс формы для работы приложения ckeditor
    form = PostAdminForm
    save_on_top = True
    # Зададим поля, отображаемые в админке
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo', 'views')
    # Обозначим поля, ссылающие на редактирование поста
    list_display_links = ('id', 'title')
    # Возможность поиска по заданным полям
    search_fields = ('title',)
    # Фильтр по заданным полям
    list_filter = ('category', 'tags')
    # Поля для чтения
    readonly_fields = ('views', 'created_at', 'get_photo')
    # Поля при редактировании поста
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at')

    # Создадим функцию для отображения миниатюрной фотографии в админке
    def get_photo(self, obj):
        # Проверяем существование фотографии
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    # Зададим название полю в админке
    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    # Атрибут prepopulated_fields автоматически сгенерирует нам slug на основе title
    prepopulated_fields = {"slug": ("title",)}
    # Зададим поля, отображаемые в админке
    list_display = ('id', 'title', 'slug')
    # Обозначим поля, ссылающие на редактирование поста
    list_display_links = ('id', 'title')
    # Возможность поиска по заданным полям
    search_fields = ('title',)


class TagAdmin(admin.ModelAdmin):
    # Атрибут prepopulated_fields автоматически сгенерирует нам slug на основе title
    prepopulated_fields = {"slug": ("title",)}
    # Зададим поля, отображаемые в админке
    list_display = ('id', 'title', 'slug')
    # Обозначим поля, ссылающие на редактирование поста
    list_display_links = ('id', 'title')
    # Возможность поиска по заданным полям
    search_fields = ('title',)


# Регистрируем модели, чтобы они появились в админке
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
