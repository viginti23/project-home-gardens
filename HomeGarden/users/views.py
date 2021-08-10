from home.decorators import unauthenticated_user
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
# Create your views here.

@unauthenticated_user
def register_or_login(request, *args, **kwargs):
    if request.method == 'POST':
        if 'register' in request.POST:
            user_register_form = UserRegisterForm(request.POST)
            if user_register_form.is_valid():
                user_register_form.save()
                messages.success(request, 'Twoje konto zostało utworzone! Możesz się teraz zalogować.')
                return redirect('login')
        if 'login' in request.POST:
            user_login_form = UserLoginForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, 
            password=password)
            if user:
                login(request, user)
                messages.success(request, 'Jesteś teraz zalogowany.')
                return redirect('offerlist')
    user_register_form = UserRegisterForm()
    user_login_form = UserLoginForm()
    template_name = 'users/register_or_login.html'
    context = {'user_register_form': user_register_form, 'user_login_form': user_login_form}
    return render(request, template_name, context)
