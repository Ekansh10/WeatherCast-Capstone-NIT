from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('register/', views.registrationPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.LogoutPage, name="logout"),
    path("result", views.result, name="result"),
    # path('social_links', views.social_links),
]
