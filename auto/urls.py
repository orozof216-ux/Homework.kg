from django.urls import path
from . import views

app_name = 'auto'

urlpatterns = [
    path('', views.auto_view, name='auto'),
]