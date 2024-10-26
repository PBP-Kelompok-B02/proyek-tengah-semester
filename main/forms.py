from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'block w-72 py-2.3 px-1 text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none placeholder-white placeholder-opacity-90 dark:focus:border-[#102C57] focus:outline-none focus:ring-0 focus:text-white focus:border-[#102C57] peer'
        })
    )
    
    password2 = forms.CharField(
        label=("Password Confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'block w-72 py-2.3 px-1 text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none placeholder-white placeholder-opacity-90 dark:focus:border-[#102C57] focus:outline-none focus:ring-0 focus:text-white focus:border-[#102C57] peer'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'block w-full py-2.3 px-1 text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none placeholder-white placeholder-opacity-90 dark:focus:border-[#102C57] focus:outline-none focus:ring-0 focus:text-white focus:border-[#102C57] peer'
            }),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
        

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()