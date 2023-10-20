
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/',views.register, name='register_user'),
    path('yourprofile/',views.profile, name='profile'),
   # path('update_profile/<str:pk>/',views.UpdateProfile.as_view(), name='update_profile'),

   path('accounts/update_profile/',views.updating_profile_info, name='update_profile_info'),

   # change password 
  path('change_password/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),name='change_password'),
   path('change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done'),

   # Password Reset

   path('password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html'),name='reset_password'),
   path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_done.html'),name='password_reset_done'),
   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_confirm.html'), name='password_reset_confirm'),
   path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_complete.html'),name='reset_complete'),
   

   


    
]