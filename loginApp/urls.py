from django.urls import path
from .views import *
from django.contrib.auth import views
urlpatterns = [ 
    path ('index/',index, name = 'user_list'),
    path ('', Auth.as_view(), name='auth_list' ),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
 
]


