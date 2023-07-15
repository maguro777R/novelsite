from typing import Any, Dict, Optional
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, FormView, View, DeleteView
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, SignUpForm, LoginForm, UsernameChangeForm

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'app/post_edit.html', {'form': form})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'app/post_edit.html', {'form': form})

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "app/signup.html"
    success_url = reverse_lazy("post_list")

    def from_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())
    
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='user')
    else:
        form = SignUpForm()
    param = {
        'form': form
    }
    return render(request, 'app/signup.html', param)

def login_view(request):
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                if next == 'None':
                    return redirect(to='/user/')
                else:
                    return redirect(to=next)
    else:
        form = LoginForm()
        next = request.GET.get('next')

    param = {
        'form': form,
        'next': next
    }
    return render(request, 'app/login.html', param)

def logout_view(request):
    logout(request)
    return render(request, 'app/logout.html')

@login_required
def user_view(request):
    user = request.user

    params = {
        'user': user
    }

    return render(request, 'app/user.html', params)

@login_required
def other_view(request):
    users = User.objects.exclude(username=request.user.username)

    params = {
        'users': users
    }

    return render(request, 'app/other.html', params)

class UsernameChangeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        form = UsernameChangeForm()
        context["form"] = form
        return render(request, 'app/change_username.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = UsernameChangeForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            user_obj = User.objects.get(username=request.user.username)
            user_obj.username = username
            user_obj.save()
            messages.info(request, "usernameを変更しました。")

            return redirect('user')
        else:
            context["form"] = form

            return render(request,'app/change_username.html', context)
        
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.username == self.kwargs['username'] or user.is_superuser
    
class UserDeleteView(OnlyYouMixin, DeleteView):
    template_name = "app/delete.html"
    success_url = reverse_lazy("login")
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'

def user_post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/user_post_list.html', {'posts': posts})

@require_POST
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('user_post_list')