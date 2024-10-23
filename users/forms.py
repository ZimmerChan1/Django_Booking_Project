from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import CustomUser
from django import forms


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Введите имя пользователя"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Введите пароль"
    }))

    class Meta:
        model = CustomUser
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):



    username = forms.CharField(widget=forms.TextInput(attrs={

        "placeholder": "Введите имя пользователя"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={

        "placeholder": "Введите Email"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={

        "placeholder": "Введите пароль"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={

        "placeholder": "Подтвердите пароль"
    }))

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")


class UserProfileForm(UserChangeForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "readonly": True,
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control py-4",
        "readonly": True,
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
    }))

    # Измените 'image' на 'profile_image'
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={
    }))

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "profile_image")
