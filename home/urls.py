from django.urls import path
from .views import BookingListView, RoomDetailView, BookingFormView

urlpatterns = [
    path('', BookingFormView.as_view(), name='home'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('room/<id>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(),
         name='CancelBookingView'),
    
]
