from django.views.generic import TemplateView
from django.shortcuts import render


def main_pg_view(request):
    title = 'SirCianid Games'
    text0 = 'Главная страница'
    context = {
        'title': title,
        'text0': text0,
    }
    return render(request, 'fourth_task/menu.html', context)


def games_shp_page(request):
    title = 'Наш Магазин'
    text0 = 'Каталог Игр:'
    text1 = 'Быстрая покупка'
    text2 = 'Добавить в корзину'
    games = ['Atomic Heart:Gold Edition', 'METRO Exodus:Enhanced Edition', 'Cyberpunk 2077:Ultimate Edition',
             'Call Of Duty: MW3 Remastered']
    context = {
        'title': title,
        'text0': text0,
        'text1': text1,
        'text2': text2,
        'games': games
    }
    return render(request, 'fourth_task/games.html', context)


def cart_page(request):
    title = 'Ваша Корзина Товаров'
    text0 = 'Корзина: '
    text1 = 'Похоже, в вашей корзине еще нет товаров. Нужно это исправить!'
    context = {
        'title': title,
        'text0': text0,
        'text1': text1
    }
    return render(request, 'fourth_task/cart.html', context)
