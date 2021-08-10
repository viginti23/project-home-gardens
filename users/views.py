from home.decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, AccountUpdateForm
from django.contrib import messages


# Create your views here.


@unauthenticated_user
def register_or_login(request, *args, **kwargs):
    if request.method == 'POST':
        if 'register' in request.POST:
            user_register_form = UserRegisterForm(request.POST)
            if user_register_form.is_valid():
                user_register_form.save()
                username = user_register_form.cleaned_data['username']
                messages.success(
                    request, f'Konto {username} zostało utworzone! Możesz się teraz zalogować.')
                return redirect('login')

        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Jesteś teraz zalogowany.')
                return redirect('login')

    user_register_form = UserRegisterForm()
    user_login_form = UserLoginForm()
    template_name = 'users/register_or_login.html'
    context = {'user_register_form': user_register_form, 'user_login_form': user_login_form, 'request': request}
    return render(request, template_name, context)


@login_required(login_url='login')
def my_account(request, id):
    if request.user.id == id:
        user = User.objects.get(id=id)
        if request.method == 'POST':
            user_update_form = UserUpdateForm(request.POST, instance=user)
            account_update_form = AccountUpdateForm(
                request.POST, request.FILES, instance=user.account)
            pic = request.FILES.get('image')
            if user_update_form.is_valid() and account_update_form.is_valid():
                user_update_form.save()
                account_update_form.save()
        user_update_form = UserUpdateForm(instance=user)
        account_update_form = AccountUpdateForm(instance=user)
        template = 'users/account/account.html'
        context = {
            'user_update_form': user_update_form,
            'account_update_form': account_update_form,
        }
        return render(request, template, context)
    return redirect('profile')


def profile(request, id):
    template = 'users/profile.html'
    context = {}
    return render(request, template, context)

# @login_required
# def my_account
# - username update
# - password update
# - image update
# zarządzanie ofertami:
# - lista ofert z checkboxami USUŃ OGŁOSZENIE |
# - wiadomości


# def profile
# formularz kontakowy
# zdjęcie
# dane
# oferty
