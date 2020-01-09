from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='GitHubInfo'),
    path('signup/', views.signup, name='SignUp'),
    path('login/', LoginView.as_view(), name='Login'),
    path('home/', views.home, name='Home'),
    path('logout/', LogoutView.as_view(), name='LogOut'),
    path('home2/', views.home2, name='Home2')
]
