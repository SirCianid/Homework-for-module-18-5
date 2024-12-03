from django.views.generic import TemplateView
from django.shortcuts import render


def main_pg_view(request):
    title = 'SirCianid Games'
    text0 = 'Главная страница'
    text1 = 'На главную'
    text2 = 'К магазину'
    text3 = 'В корзину'
    context = {
        'title': title,
        'text0': text0,
        'text1': text1,
        'text2': text2,
        'text3': text3,
    }
    return render(request, 'third_task/main_page.html', context)


def games_shp_page(request):
    title = 'Наш Магазин'
    text0 = 'Каталог Игр:'
    text1 = 'Быстрая покупка'
    text2 = 'Добавить в корзину'
    text3 = 'Atomic Heart:Gold Edition'
    text4 = 'METRO Exodus:Enhanced Edition'
    text5 = 'Cyberpunk 2077:Ultimate Edition'
    text6 = 'Call Of Duty: MW3 Remastered'
    text7 = 'Вернуться на главную'
    text8 = 'Перейти в корзину'
    context = {
        'title': title,
        'text0': text0,
        'text1': text1,
        'text2': text2,
        'text3': text3,
        'text4': text4,
        'text5': text5,
        'text6': text6,
        'text7': text7,
        'text8': text8
    }
    return render(request, 'third_task/games.html', context)


def cart_page(request):
    title = 'Ваша Корзина Товаров'
    text0 = 'Корзина: '
    text1 = 'Похоже, в вашей корзине еще нет товаров. Нужно это исправить!'
    text2 = 'Обратно в магазин'
    text3 = 'Вернуться на главную'
    context = {
        'title': title,
        'text0': text0,
        'text1': text1,
        'text2': text2,
        'text3': text3,
    }
    return render(request, 'third_task/cart.html', context)