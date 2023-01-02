from django.core.exceptions import ValidationError


def get_path_to_image(instance, file):
    return f'images/{instance.id}/{file}'


def size_validator(file):
    megabyte_limit = 2
    if file.size > megabyte_limit * 1024 * 1024:
        raise ValidationError('Файл слишком много весит!!!')
