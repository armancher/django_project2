from django.urls import path

from users.views import UserRegisterView, UserLoginView, UserLogoutView, HomeView

app_name = 'users'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
]
