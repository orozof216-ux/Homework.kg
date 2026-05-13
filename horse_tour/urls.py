from django.urls import path
from .views import (
    company_list,
    tour_detail,
    booking_list,
    booking_create,
    booking_update,
    booking_delete
)

urlpatterns = [
    path('', company_list, name='tour_list'),

    path('tour/<int:pk>/', tour_detail, name='tour_detail'),

    # 📌 bookings
    path('bookings/', booking_list, name='booking_list'),
    path('bookings/create/', booking_create, name='booking_create'),
    path('bookings/update/<int:id>/', booking_update, name='booking_update'),
    path('bookings/delete/<int:id>/', booking_delete, name='booking_delete'),
]