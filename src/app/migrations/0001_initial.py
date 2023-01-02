# Generated by Django 4.1.4 on 2023-01-02 14:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import src.base.services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=src.base.services.get_path_to_image, validators=[src.base.services.size_validator, django.core.validators.FileExtensionValidator(allowed_extensions=('jpg',))])),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Категория')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
