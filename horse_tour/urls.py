from django.urls import path
from .views import (
    CompanyListView,
    TourDetailView,
    BookingListView,
    BookingCreateView,
    BookingUpdateView,
    BookingDeleteView
)

urlpatterns = [
    path('', CompanyListView.as_view(), name='tour_list'),  

    path('tour/<int:pk>/', TourDetailView.as_view(), name='tour_detail'), 

    path('bookings/', BookingListView.as_view(), name='booking_list'),  

    path('bookings/create/', BookingCreateView.as_view(), name='booking_create'),  

    path('bookings/update/<int:pk>/', BookingUpdateView.as_view(), name='booking_update'),  

    path('bookings/delete/<int:pk>/', BookingDeleteView.as_view(), name='booking_delete'),  
]