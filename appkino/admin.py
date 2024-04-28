from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(modelActor)
admin.site.register(modelDirector)
admin.site.register(modelGenre)
# admin.site.register(modelOtziv)

class adminPodpiska(admin.ModelAdmin):
    list_display = ('name','price')

admin.site.register(modelPodpiska,adminPodpiska)

class adminKino(admin.ModelAdmin):
    list_display = ('name','director','year','podpiska')
    fieldsets = (('О фильме',{
        'fields':('name','info','year','genre','country')
    }),
                 ('Люди',{
        'fields':('actor','director')
    }),
                 ('Для сайта',{
        'fields':('poster','rating','podpiska','file')
    })
                 )
admin.site.register(modelKino,adminKino)

class adminOtziv(admin.ModelAdmin):
    list_display = ('user','film')

admin.site.register(modelOtziv,adminOtziv)