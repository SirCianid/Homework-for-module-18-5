from django import forms
from django.core.exceptions import ValidationError

users = ["john_doe", "jane_smith", "peter_jones"]


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Введите логин", required=True)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Введите пароль", required=True)
    repeat_password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Повторите пароль", required=True)
    age = forms.IntegerField(label="Введите возраст", min_value=0, required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")
        age = cleaned_data.get("age")
        username = cleaned_data.get("username")

        if password != repeat_password:
            raise forms.ValidationError("Пароли не совпадают")
        if age < 18:
            raise forms.ValidationError("Вы должны быть старше 18")
        if username in users:
            raise forms.ValidationError("Пользователь уже существует")
        return cleaned_data


