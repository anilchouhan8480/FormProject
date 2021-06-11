from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .forms import MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('appp2/', include('appp2.urls')),
    path('app3/', include('app3.urls')),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="passwordreset/password_reset.html",form_class=MyPasswordResetForm),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="passwordreset/password_reset_done.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="passwordreset/password_reset_confirm.html",form_class=MySetPasswordForm), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="passwordreset/password_reset_complete.html"), 
        name="password_reset_complete"),

]
