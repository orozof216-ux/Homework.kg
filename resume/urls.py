from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    ResumeListView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  
    path('login/', LoginView.as_view(), name='login'),           
    path('logout/', LogoutView.as_view(), name='logout'),       
    path('', ResumeListView.as_view(), name='resume_list'),      
]