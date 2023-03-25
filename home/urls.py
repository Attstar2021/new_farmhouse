from django.urls import path
from .views import BookingListView, RoomDetailView, BookingFormView, CancelBookingView
from django.conf import settings

urlpatterns = [
    path('', BookingFormView.as_view(), name='home'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(),
         name='CancelBookingView'),
    
]
