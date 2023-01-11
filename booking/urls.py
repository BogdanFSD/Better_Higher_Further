from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_training, name='booking'),
    path('Booked', views.check_booked_training,
         name='booked'),
    path('Edit/<int:booking_id>', views.edit, name='edit'),
    path('delete_booking<booking_id>/', views.delete_booking, name='delete_booking'),
]
