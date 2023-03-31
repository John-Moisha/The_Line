import os

from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import HiddenInput
from django.template.defaultfilters import filesizeformat
from .models import CustomUser
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import gettext_lazy as _
from django.core.validators import *


# class SettingsForm(forms.ModelForm):
#     error_css_class = 'is-invalid'
#
#     avatar = forms.FileField(
#         label="Аватар",
#         validators=[
#             FileExtensionValidator(
#                 allowed_extensions=['jpg', 'jpeg', 'png', 'exe'],
#                 message=_('Разрешение файлов дожно быть JPG, JPEG, PNG')),
#         ],
#         widget=forms.FileInput(
#             attrs={
#                 "class": "file-field fileinput fileUpload form-control-file",
#             }
#         )
#     )
#     first_name = forms.CharField(
#         label="Имя",
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     last_name = forms.CharField(
#         label="Фамилия",
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     email = forms.EmailField(widget=forms.EmailInput(
#         attrs={
#             "class": "form-control"
#         }
#     ))
#
#
#     class Meta:
#         model = CustomUser
#         fields = (
#             'avatar',
#             'first_name',
#
#         )


class SettingsForm(forms.ModelForm):
    error_css_class = 'is-invalid'

    avatar = forms.FileField(
        label="Аватар",
        required=False,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png', 'exe'],
                message=_('Разрешение файлов дожно быть JPG, JPEG, PNG')),
        ],
        widget=forms.FileInput(
            attrs={
                "class": "file-field fileinput fileUpload form-control-file",
            }
        )
    )
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        label='E-mail',
        required=False,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "readonly": True,
            }
        )
    )
    password1 = forms.CharField(
        label='Пароль',
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
            }
        )

    )
    password2 = forms.CharField(
        label='Повторите пароль',
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
            }
        )

    )

    class Meta:
        model = CustomUser
        fields = (
            # 'avatar',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            self.add_error('password2', 'Пароли не совпадают')

        return cleaned_data


class SighUpForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control"
        }
    ))
    password1 = forms.CharField(min_length=6, widget=forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
    ))
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
    ))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            self.add_error('password2', 'Passwords should match!')

        return cleaned_data

    def save(self, commit=True):
        # instance: CustomUser = super().save(commit=False)
        instance: CustomUser = super().save(commit=True)
        instance.is_active = True
        # instance.is_active = False
        instance.set_password(self.cleaned_data['password1'])

        if commit:
            # breakpoint()
            instance.save()

        # token = default_token_generator.make_token(instance) #todo
        # send_activate_account_email.delay(instance.username, token) #todo

        return instance


class LogInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LogInForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ваша почта',
        })
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ваш пароль',
        })
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'password',)


