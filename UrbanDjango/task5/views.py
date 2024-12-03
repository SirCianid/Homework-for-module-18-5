from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

users = ["john_doe", "jane_smith", "peter_jones"]


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            return HttpResponse(f"Приветствуем, {username}!")
        else:
            info['error'] = form.errors.as_text()  # выводим все ошибки формы
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'fifth_task/reg_page.html', {'users': users, 'info': info})


def sign_up_by_html(request):
    info = {}
    users_list = users

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age_str = request.POST.get('age')

        try:
            age = int(age_str)
        except ValueError:
            info['error'] = 'Неверный формат возраста'
            return render(request, 'fifth_task/reg_page.html', {'users': users_list, 'info': info})

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return HttpResponse(f"Приветствуем, {username}!")
    return render(request, 'fifth_task/reg_page.html', {'users': users_list, 'info': info})
