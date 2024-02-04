# user_auth/urls.py
from django.urls import path
from .views import register_user, login_user, logout_user
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('index/', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact")

    # ... other authentication URLs as needed
]
