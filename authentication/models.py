from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Модель: Переопределяем модель пользователя """

    # Пол пользователей:
    MALE = 'm'
    FEMALE = 'f'
    SEX = [(MALE, 'Male'), (FEMALE, 'Female')]

    # Роли пользователей:
    ADMINISTRATOR = 'administrator'
    MODERATOR = 'moderator'
    EMPLOYEE = 'employee'
    UNKNOWN = 'unknown'
    ROLE = [(MODERATOR, 'Moderator'), (EMPLOYEE, 'employee'), (UNKNOWN, 'unknown')]

    sex = models.CharField(verbose_name='Пол пользователя', max_length=1, choices=SEX, default=MALE)
    role = models.CharField(verbose_name='Роль пользователя', max_length=9, choices=ROLE, default=UNKNOWN)
