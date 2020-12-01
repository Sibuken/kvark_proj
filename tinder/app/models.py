from django.db import models
from django.contrib.auth.models import AbstractUser


# Наследуем модель Юзера
class User(AbstractUser):
    # Какие атрибуты можно еще добавить?
    type_of_inv = models.CharField(max_length=20)


# Создание модели стартапа
class Startup(models.Model):
    name_of_startup = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField(max_length=15)
    video = models.FileField(upload_to='videos/%Y/%m/%d/')
    desk = models.CharField(max_length=500)      # Или TextField?
    pitch_deck = models.FileField(upload_to='pitch_decks/%Y/%m/%d/')
    members = models.ManyToManyField(User, through='InvestorsChoice')


class Slide(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')


# Промежуточная таблица отобранных проектов
class InvestorsChoice(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    response = models.BooleanField()
