from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request): #функция для вывода на экран страницы приветствия
    return HttpResponse ("<h1>Будьте бдительны, удача не пройдет мимо! 🦸‍♂️ </h1>")

def new(request): #функция для вывода на экран страницы приветствия
    return HttpResponse ("<h1>Теперь проходите! 🦸‍♂️ </h1>")

