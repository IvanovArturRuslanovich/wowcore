from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'core/index.html', {'title':'Главная страница'})


def about(request):
    return render(request, 'core/about.html', {'title': 'О сайте'})


def categories(request, catid):
    print(request.GET)
    return HttpResponse(f"<h1>Список товаров на аукционе</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')




