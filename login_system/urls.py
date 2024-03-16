from django.urls import path, include
from login_system import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),
    
    
]
