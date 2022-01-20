from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


def register_account(request):
    if request.method == 'GET':
        return render(request, 'account/register_account.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('account:profileuser')
            except IntegrityError:
                return render(request, 'account/register_account.html',
                              {'form': UserCreationForm(), 'error': 'Пользователь уже существует'})
        else:
            return render(request, 'account/register_account.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})



def login_account(request):
    if request.method == 'GET':
        return render(request, 'account/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'account/login.html',
                          {'form': AuthenticationForm(),
                           'error': 'Пользователь или пароль не определены. Пройди регистрацию'})
        else:
            login(request, user)
            return redirect('account:profileuser')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homeapp:homepage')

@login_required
def profileuser(request):
    return render(request, 'account/profileuser.html')