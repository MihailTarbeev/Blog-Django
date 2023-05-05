from django import template
from blog.models import Post, Tag


# Регистрируем библиотеку
register = template.Library()


# Создаём тэг, который будет возвращать популярные посты
@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular_posts(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}


# Создаём тэг, который будет возвращать все теги поста
@register.inclusion_tag('blog/tags_tpl.html')
def get_tags(cnt=25):
    tags = Tag.objects.all()[:cnt]
    return {'tags': tags}
