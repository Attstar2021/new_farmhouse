from django.urls import path
from .views import BookingListView, RoomDetailView, BookingFormView

urlpatterns = [
    path('', BookingFormView.as_view(), name='home'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
]
