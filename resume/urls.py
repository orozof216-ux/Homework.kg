from django.urls import path
from .views import register_view, resume_list, login_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', resume_list, name='resume_list'),
]