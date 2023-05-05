from django import template
from blog.models import Category


# Регистрируем библиотеку
register = template.Library()


# Создаём тэг, который будет возвращать все категории
@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    # Присвоим переменной все объекты категории
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}
