from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


    def clean(self):
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        email = self.cleaned_data.get('email')


        if password1 != password2:
            self.add_error('password1', '비밀 번호가 일치하지 않습니다.')

        try:
            User = get_user_model()
            User.objects.get(username=username)
            self.add_error('username', '이미 가입된 아이디입니다.')

        except:
            pass
