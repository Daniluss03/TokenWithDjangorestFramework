from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='singup'),
    path('test_token/', views.test_token, name='test_token'),
]