from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView,
    PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView)
app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>', views.profile, name='profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('change-password/', views.change_password, name='change-password'),
    path('reset-password/', PasswordResetView.as_view(
         template_name='account/reset_password.html',
         email_template_name='account/reset_password_email.html',
         success_url=reverse_lazy('account:password_reset_done')),
         name='reset-password'),
    path('reset-password/done/', PasswordResetDoneView.as_view(
         template_name='account/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
         template_name='account/password_reset_confirm.html',
         success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(
         template_name='account/password_reset_complete.html',),
         name='password_reset_complete'),
]
