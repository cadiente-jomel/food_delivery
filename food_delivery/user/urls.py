from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login_page, name='login-page'),
    path('register/', views.register_page, name='register-page'),
    path('profile/', views.profile_page, name='profile-page'),
    path('profile_upload/', views.profile_upload, name='profile-upload-page'),
]
