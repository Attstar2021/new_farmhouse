from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.booking_form, name='home'),
    path('booking_list/', views.BookingListView.as_view(), name='BookingListView'),
    path('delete/<booking_id>', views.delete_booking,
         name='delete'),
    path('', include('blog.urls')),
]
