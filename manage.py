#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
     main()

     Что сделал:
Я создал приложение “конный тур”, сделал модели (человек, конь, компания, отзывы, услуги), настроил связи OneToOne, OneToMany и ManyToMany. Также добавил вывод компаний и среднего рейтинга на HTML страницу и сделал красивый дизайн через Bootstrap.

Проблема:
Сначала не отображались данные на странице и были ошибки при добавлении в админке (не понимал связи и обязательные поля).

Что буду делать:
Буду дальше практиковаться с Django, лучше разбираться в связях моделей и улучшать дизайн сайта.