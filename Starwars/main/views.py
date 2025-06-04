from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>Это главная страница моего первого проекта Starwars на Django</h1>")


def data(request):
    return HttpResponse("<h1>Страница данных: Здесь отображается важная информация!</h1>")

def test(request):
    return HttpResponse("<h1>Это Тестовая страница: Проверка работы приложения!</h1>")


