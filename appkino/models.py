from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class modelGenre(models.Model):
    name = models.CharField(max_length=30, verbose_name='Жанр')

    def __str__(self):
        return self.name

class modelActor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Актер')
    info = models.TextField(verbose_name='Информация', null=True, blank=True)
    foto = models.FileField(blank=True, null=True,
                              verbose_name='Фото',
                              upload_to='fotoActor/',
                              )
    def __str__(self):
        return self.name

    def getUrl(self):
        return f'{self.id}/'

class modelDirector(models.Model):
    name = models.CharField(max_length=100, verbose_name='Режиссер')
    info = models.TextField(verbose_name='Информация', null=True, blank=True)
    foto = models.FileField(blank=True, null=True,
                              verbose_name='Фото',
                              upload_to='fotoDirector/',
                              )
    def __str__(self):
        return self.name

    def getUrl(self):
        return f'{self.id}/'

class modelPodpiska(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    price = models.IntegerField(verbose_name='Стоимость')

    def __str__(self):
        return self.name



class modelKino(models.Model):
    poster = models.FileField(blank=True, null=True,
                                  verbose_name='Постер',
                              upload_to='posters/',
                              )
    name = models.CharField(max_length=50,
                            verbose_name='Название')
    genre = models.ForeignKey(to=modelGenre, on_delete=models.SET_NULL,
                              null=True,
                              verbose_name='Жанр')
    director = models.ForeignKey(to=modelDirector, on_delete=models.SET_NULL,
                                 null=True,
                            verbose_name='Режиссер')
    country = models.CharField(max_length=50, blank=True, null=True,
                            verbose_name='Страна')
    year = models.IntegerField(blank=True, null=True,
                            verbose_name='Год')
    actor = models.ManyToManyField(to=modelActor,
                            verbose_name='Актеры')
    rating = models.FloatField(blank=True, null=True,
                            verbose_name='Рейтинг')
    info = models.TextField(blank=True, null=True,
                            verbose_name='Информация')
    podpiska = models.ForeignKey(to=modelPodpiska, on_delete=models.SET_DEFAULT,
                                 default=1, null=True,
                            verbose_name='Подписка')
    file = models.URLField(blank=True, null=True,
                           verbose_name='Трейлер')
    # otziv = models.ManyToManyField(to=modelOtziv)

    def __str__(self):
        return self.name

    # def getPodpiska(self):
    #     item = self.podpiska
    #     str=''
    #     str+=self.name
    #     return str

    def getUrl(self):
        return f'{self.genre}/{self.id}/'
    def getUrl2(self):
        return f'kino/{self.genre}/{self.id}/'
    def getOtziv(self):
        return self.modelotziv_set.all()
    def getForm(self):
        from .forms import formOtziv
        return formOtziv()

class modelProfile(models.Model):
        user = models.OneToOneField(to=User, on_delete=models.CASCADE)
        podpiska = models.ForeignKey(to=modelPodpiska, on_delete=models.SET_DEFAULT,
                                     default=1)
        balance = models.IntegerField(default=1000)

class modelOtziv(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT,
                             default='user', verbose_name='Пользователь')
    text = models.TextField(verbose_name='Отзыв')
    film = models.ForeignKey(to=modelKino, on_delete=models.CASCADE,
                             verbose_name='Кино', null=True)
