from django.shortcuts import render
from django.http import HttpResponse
# здесь будет функция для вывода на экран страницы приветствия

def data (request): #функция для вывода на экран страницы приветствия
    return HttpResponse ("<h1>Какой сегодня день? 😍</h1>")

def test(request):
    return HttpResponse ("<h1>Ты не помнишь, какой сегодня день? Ты не прошёл тест! 🩸🪓 </h1>")