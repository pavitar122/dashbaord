from django.urls import path, include
from login_system import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),
    path('add_blog/', views.add_blog, name="add_blog"),
    path('dashboard/', views.dashbaord, name="dashboard"),
    path('blog/<str:post_title>/', views.blog, name="blog"),
    path('delete_draft/<str:post_title>/', views.delete_draft, name="delete"),
    path('Doctor_blogs/', views.doctor_blogs, name="doc_blogs"),   
    path('Patient_blogs/', views.patient_blogs, name="pat_blogs"),   
    path('api/all-blog-posts/', views.api_blog_posts, name="posts"),  
    path('api/draft-blogs/', views.api_draft_blog, name="posts"),              
]
