from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login_page, name='login-page'),
    path('register/', views.register_page, name='register-page'),
    path('profile/', views.profile_page, name='profile-page'),

    # ajax links
    path('profile_upload/', views.profile_upload, name='profile-upload-page'),
    path('add_address/', views.add_address, name='add-address'),
    path('edit_address/<str:pk>/', views.edit_address, name='edit-address'),
    path('fetch_address/<str:pk>/', views.fetch_address, name='fetch-address'),
]
