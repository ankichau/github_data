from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('lander/', views.index, name='GitHubInfo'),
    path('signup/', views.signup, name='SignUp'),
    path('login/', LoginView.as_view(), name='Login'),
    path('home/', views.home, name='Home'),
    path('logout/', LogoutView.as_view(), name='LogOut'),
]
