from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_views.register_user, name='register'),
    path('login/', user_views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('<int:pk>/my_account/', user_views.my_account, name='account'),
    path('<int:pk>/', user_views.profile, name='profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/account/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='users/account/password_reset_done.html'), name='password_reset_done'),

]
