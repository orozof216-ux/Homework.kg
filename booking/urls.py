from django.urls import path
from .views import (
    BookingListView,
    BookingCreateView,
    BookingUpdateView,      
    BookingDeleteView
)

urlpatterns = [
    path('', BookingListView.as_view(), name='booking_list'),  

    path('create/', BookingCreateView.as_view(), name='booking_create'),  

    path('update/<int:pk>/', BookingUpdateView.as_view(), name='booking_update'), 

    path('delete/<int:pk>/', BookingDeleteView.as_view(), name='booking_delete'),  
]