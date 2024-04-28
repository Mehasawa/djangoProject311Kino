from django.shortcuts import render, redirect
from .models import *
import random
# Create your views here.
def index(req):
    film = modelKino.objects.all()
    actor = modelActor.objects.all()
    randomFilm = random.choice(film)
    data = {'film':film,'actor':actor,'random':randomFilm}
    return render(req,'index.html',data)

from django.views import generic
class kinoList(generic.ListView):
    model = modelKino

class kinoDetail(generic.DetailView):
    model = modelKino

class actorList(generic.ListView):
    model = modelActor
    paginate_by = 2

class actorDetail(generic.DetailView):
    model = modelActor

from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
def registr(req):
    # forma = UserCreationForm()
    print(1)
    if req.POST:
        print(2)
        forma = formRegistr(req.POST)#форма регистрации проверка
        if forma.is_valid():#проверка пройдена
            print(3)
            #собираем данные
            k1 = forma.cleaned_data.get('username')
            k2 = forma.cleaned_data.get('password1')
            k3 = forma.cleaned_data.get('email')
            k4 = forma.cleaned_data.get('first_name')
            k5 = forma.cleaned_data.get('last_name')
            User.objects.create_user(username=k1, password=k2)#новая строка пользователь
            # user1 =  authenticate(username=k1, password=k2)
            user = User.objects.get(username=k1)#находим пользователя
            #заполняем данные
            user.email = k3
            user.last_name = k5
            user.first_name = k4
            user.save() #сохраняем
            modelProfile.objects.create(balance=1000, podpiska_id=1, user_id=user.id) #привяжет профиль пользователя
            login(req,user) #вход пользователя на сайт
            return redirect('home')#на главную
    else:
        forma = formRegistr()#форма регистрации
    data = {'form':forma}
    return render(req,'registration/registration.html',data)

def profile(req):

    return render(req,'kabinet.html')

def profileChange(req):
    forma=formPodpiska()
    data ={'form':forma}
    if req.POST:
        k1 = req.POST.get('item')
        user = User.objects.get(id= req.user.id)
        user.modelprofile.podpiska_id = k1
        user.modelprofile.save()
        return redirect('kabinet')
    return render(req,'kabinet.html',data)

def otziv(req, kinoid):
    print(1)
    # print(kinoid)
    if  req.POST: #загружается форма отзыва
        k1 = req.POST.get('text')
        k2 = req.user.id #кто написал отзыв
        k3 = req.user.username
        print(k1,k2,k3)
        film = modelKino.objects.get(id=kinoid)#находим фильм на который отзыв
        modelOtziv.objects.create(text=k1, user_id=k2, film_id=kinoid)#записывает отзыв таблицу

        return redirect('onekino',film.genre,film.id) #обновляем ту же страницу фильма
    return redirect('home')