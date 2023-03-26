from django.urls import path
from . import views
from .views import BookingListView, BookingFormView, CancelBookingView
from django.conf import settings

urlpatterns = [
    path('', BookingFormView.as_view(), name='home'),
    #path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(),
         name='CancelBookingView'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
