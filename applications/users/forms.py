from django import forms
from .models import User
from django.contrib.auth import authenticate


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir contraseña'
            }
        )
    )

    class Meta:
        model = User
        #fields = ('__all__')
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
        )

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas son diferentes!')


class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'Usuario',
        required = True,
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Usuario',
                'class': 'form-control form-control-user'
            }
        )
    )

    password = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'form-control form-control-user'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username = username, password = password):
            raise forms.ValidationError('Los datos del usuario no son correctos')
        
        return self.cleaned_data


        

