from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text', 'status',)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class LoginForm(AuthenticationForm):
    pass

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]

        def __init__(self, *args, **kargs):
            super().__init__(*args, **kargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = "form-control"
                field.widget.attrs['placeholder'] = "150 characters or fewer. Letters, digits and @/./+/-/_ only."