from django.urls import path, include
from knox import views as knox_views
from django.contrib.auth import views as auth_views
from .api import *
from .views import *
from . import views

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('user/', UserAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='Knox_logout'),
    path('change_password/', ChangePasswordView.as_view()),
    path('knox/', include('knox.urls')),
    path('reset_password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
    path('activate', auth_views.PasswordResetDoneView.as_view(), name="activate"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('AccountSuccess/', views.ActivateAccount, name="AccountSuccess"),
]
