from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import HiddenInput

from library.models import book, Supplier, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ['name', 'description', 'pages', 'price', 'cover_type', 'size', 'date_publication', 'photo', 'supplier']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'pages': forms.NumberInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'cover_type': forms.TextInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'size': forms.TextInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'date_publication': forms.DateInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'photo': forms.FileInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'supplier': forms.Select(
                attrs={
                    'class': 'input_box',
                }
            ),
        }

    # Валидация
    # required=True - обязательное поле
    # max_length - максимальная длина текста
    # min_length - минимальная длина текста
    # max_value - максимальное значение числа
    # max_value - минимальное значение числа
    # step_size - шаг при установки числового значения

    # Стили
    # label - Вывод названия
    # widget - Указания типа поля
    # initial - Значение по умолчанию
    # help_text - подсказка под полем


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['title', 'agent_firstname', 'agent_name', 'agent_patronymic', 'exist']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин'
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )


class EditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def pas(self):
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = HiddenInput()

# email
class ContactForm(forms.Form):
    # recipient = forms.EmailField(
    #     label='Получатель',
    #     required=False,
    #     widget=forms.EmailInput(
    #         attrs={'class': 'form-control'}
    #     )
    # )
    subject = forms.CharField(
        label='Тема письма',
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    content = forms.CharField(
        label='Тело письма',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 8
            }
        )
    )


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_firstname', 'author_name', 'author_patronymic', 'biography', 'photo', 'date_of_birth', 'date_of_death']
        #
        # widgets = {
        #     'author_firstname': forms.TextInput(
        #         attrs={
        #             'class': 'input_box',
        #         }
        #     ),
        #     'author_name': forms.TextInput(
        #         attrs={
        #             'class': 'input_box',
        #         }
        #     ),
        #     'author_patronymic': forms.TextInput(
        #         attrs={
        #             'class': 'input_box',
        #         }
        #     ),
        #     'biography': forms.TextInput(
        #         attrs={
        #             'class': 'input_box',
        #         }
        #     ),
        #
        #     'photo': forms.FileInput(
        #         attrs={
        #             'class': 'input_box',
        #         }
        #     ),
        #     'date_of_birth': forms.DateInput(
        #         attrs={
        #             'class': 'input_box',
        #         }
        #     ),
        #     'date_of_death': forms.DateInput(
        #         attrs={
        #             'class': 'input_box',
        #         }
        #     )
        # }