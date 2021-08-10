from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register', user_views.register_or_login, name='register'),
    path('login', user_views.register_or_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]
