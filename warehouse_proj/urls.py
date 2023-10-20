
from django.contrib import admin
from django.urls import path,include

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('apps.accounts.urls')),
    path('stock/',include('apps.stock_app.urls')),

    path('',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login_user'),
    path('accounts/logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout_user'),



]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
