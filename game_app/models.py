from datetime import date

from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

from authentication.models import User

# ------ Validators for models Game_app ----- #

def check_game_date_release(value: date):
    """ Validators: проверяем дату релиза игры """

    if value < date.today():
        raise ValidationError(f"{value} is in the past.")



# ----- Models for Game_app ----- #

class Studio(models.Model):
    """ Модель: Студия-разработчик игры """

    name = models.CharField(verbose_name='Название студии', max_length=30)
    poster = models.ImageField(verbose_name='Постер студии', upload_to='game_site_django/game_poster', blank=True, null=True)
    url = models.SlugField(verbose_name='Ссылка на студию', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студия'
        verbose_name_plural = 'Студии'
        ordering = ['name']


class Author(models.Model):
    """ Модель: Автор-разработчик игры """

    name = models.CharField(verbose_name='Имя автора', max_length=30)
    age = models.IntegerField(verbose_name='Возраст автора')
    country = models.CharField(verbose_name='Страна/Родина автора', max_length=20, blank=True, null=True)
    poster = models.ImageField(verbose_name='Постер автора', upload_to='game_site_django/author_poster', blank=True, null=True)
    url = models.SlugField(verbose_name='Ссылка на автора', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']


class Genre(models.Model):
    """ Модель: Жанр игры """

    name = models.CharField(verbose_name='Название жанра', max_length=30)
    descriptions = models.TextField(verbose_name='Описание жанра', blank=True, null=True)
    url = models.SlugField(verbose_name='Ссылка на жанр', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering =['name']


class SystemRequirements(models.Model):
    """ Модель: Системные требования игры """

    name_cpu = models.CharField(verbose_name='Название CPU', max_length=30)
    name_gpu = models.CharField(verbose_name='Название GPU', max_length=30)
    amount_type_memory = models.CharField(verbose_name='Объем и тип ОЗУ', max_length=30)
    os = models.CharField(verbose_name='Название ОС', max_length=30)

    def __str__(self):
        return self.name_cpu

    class Meta:
        verbose_name = 'Системные требования к игре'
        verbose_name_plural = 'Системные требования к игре'


class Game(models.Model):
    """ Модель: Игра """

    name = models.CharField(verbose_name='Название игры', max_length=30)
    descriptions = models.TextField(verbose_name='Описание игры', blank=True, null=True)
    poster = models.ImageField(verbose_name='Постер игры', upload_to='game_site_django/game_poster', blank=True, null=True)
    studio = models.ForeignKey('Studio', on_delete=models.DO_NOTHING, null=True,  blank=True)
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING, null=True,  blank=True)
    genre = models.ForeignKey('Genre', on_delete=models.DO_NOTHING, null=True,  blank=True)
    system_requirements = models.OneToOneField('SystemRequirements', on_delete=models.CASCADE, null=True,  blank=True,
                                               unique=False)
    date_add_game = models.DateTimeField(verbose_name='Дата добавления книги на сайт', auto_now_add=True, null=True)
    date_release = models.DateField(verbose_name='Дата выхода игры', validators=[check_game_date_release],
                                        null=True,  blank=True,)
    price = models.IntegerField(verbose_name='Цена игры')
    like = models.IntegerField(verbose_name='Like игры', default=0,
                               validators=[validators.MinValueValidator(0, 'Minimum value for like is 0.')])
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    draft = models.BooleanField(verbose_name='Релиз игры', default=False)
    url = models.SlugField(verbose_name='Ссылка на игру', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['name']
