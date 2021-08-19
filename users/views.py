from home.decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, AccountForm
from django.contrib import messages

# Create your views here.

@unauthenticated_user
def login_user(request, *args, **kwargs):
    user_login_form = UserLoginForm()
    template_name = 'users/login.html'
    context = {'user_login_form': user_login_form, 'request': request}
    if request.method == 'POST':
        # if 'loginUser' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Jesteś teraz zalogowany.')
            return redirect('offerlist')
        else:
            messages.warning(request, 'Nieprawidłowy login lub hasło!')
            return redirect('login')
    return render(request, template_name, context)


@unauthenticated_user
def register_user(request, *args, **kwargs):
    if request.method == 'POST':
        # if 'registerUser' in request.POST:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            # user = User.objects.create_user(
            #     username=user_register_form.clean_data['username'],
            #     password=user_register_form.clean_data['password1'],
            #     email=user_register_form.clean_data['email'])
            user = user_register_form.save(commit=False)
            user.save()
            username = user_register_form.cleaned_data['username']
            messages.success(request, f'Konto {username} zostało utworzone! Możesz się teraz zalogować.')
            return redirect('login')
    else:
        user_register_form = UserRegisterForm()
    template_name = 'users/register.html'
    context = {'user_register_form': user_register_form, 'request': request}
    return render(request, template_name, context)


@login_required(login_url='login')
def my_account(request, pk):
    if request.user.id == pk:
        # user = User.objects.get(id=pk)
        if request.method == 'POST':
            user_update_form = UserUpdateForm(request.POST, instance=request.user)
            account_form = AccountForm(
                request.POST, request.FILES, instance=request.user.account)
            # pic = request.FILES.get('image')
            if user_update_form.is_valid() and account_form.is_valid():
                user_update_form.save()
                account_form.save()
                messages.success(request, "Twoje konto zostało uaktualnione!")
        else:
            user_update_form = UserUpdateForm(instance=request.user)
            account_form = AccountForm(instance=request.user.account)
        template = 'users/account/account.html'
        context = {
                'user_update_form': user_update_form,
                'account_form': account_form,
                    }
        return render(request, template, context)
    else:
        return redirect('profile')


def profile(request, pk):
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
