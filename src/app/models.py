from django.core.validators import FileExtensionValidator
from django.db import models

from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

from ..base.services import get_path_to_image, size_validator

User = get_user_model()


class Article(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    image = models.ImageField(
        upload_to='images/%Y/%m/%d',
        validators=[
            size_validator,
            FileExtensionValidator(
                allowed_extensions=('jpg',)
            )
        ],
        blank=True,
        null=True,
        verbose_name='Ссылка на изображение'
    )
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок'
    )
    content = models.TextField(
        verbose_name='Содержимое'
    )
    date_add = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_image(self):
        if self.image:
            return mark_safe(f'<img src={self.image.url} width="100">')
        return 'Нет изображения'
    get_image.short_description = 'Изображение'


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
