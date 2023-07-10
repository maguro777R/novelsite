from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text',)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class LoginForm(AuthenticationForm):
    pass

class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ["username"]

        def __init__(self, username=None, *args, **kargs):
            kargs.setdefault('label_suffix', '')
            super().__init__(*args, **kargs)
            # ユーザーの更新前情報をフォームに挿入
            if username:
                self.fields['username'].widget.attrs['value'] = username

        def update(self, user):
            user.username = self.cleaned_data['username']