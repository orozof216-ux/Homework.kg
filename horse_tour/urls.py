from django.urls import path
from .views import (
    company_list,
    booking_list,
    booking_create,
    booking_update,
    booking_delete
)

urlpatterns = [
    path('', company_list),

    path('bookings/', booking_list, name='booking_list'),
    path('bookings/create/', booking_create, name='booking_create'),
    path('bookings/update/<int:id>/', booking_update, name='booking_update'),
    path('bookings/delete/<int:id>/', booking_delete, name='booking_delete'),
]