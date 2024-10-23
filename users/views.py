from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required  # Для защиты профиля
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


# Вход пользователя
def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # Используем cleaned_data вместо request.POST напрямую
            password = form.cleaned_data['password']  # cleaned_data проверяет и очищает данные
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))  # Перенаправление на главную
        else:
            print(form.errors)  # Выводим ошибки в консоль для отладки
    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "users/login.html", context)

# Регистрация пользователя
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()  # Сохраняем нового пользователя
            return HttpResponseRedirect(reverse('users:login'))  # Перенаправление на страницу логина
        else:
            print(form.errors)  # Показываем ошибки в консоли для отладки
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "users/register.html", context)

# Личный кабинет (только для авторизованных пользователей)

@login_required
def profile(request):
    if request.method == 'POST':  # Обработка данных из формы
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()  # Сохраняем данные профиля пользователя
            return redirect('profile')  # Перенаправление на страницу профиля после успешного сохранения
    else:
        form = UserProfileForm(instance=request.user)  # Передача текущего пользователя в форму

    return render(request, 'users/profile.html', {'form': form})

