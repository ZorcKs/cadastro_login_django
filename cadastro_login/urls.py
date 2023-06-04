from django.contrib import admin
from django.urls import path,include
from authenticate import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/',views.cadastro, name='url_cadastro'),
    path('login/',views.login, name='url_login'),
    path('',include('django.contrib.auth.urls')),
    path('',views.inicial, name='url_inicial'),
    #   URLs para redefinição de senha.
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="usuarios/password_reset.html"), name="reset_password")
]
