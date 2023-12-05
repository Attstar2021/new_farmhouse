from django.urls import path, include
from . import views
# from .views import BookingListView, BookingFormView, CancelBookingView
from django.conf import settings

urlpatterns = [
    path('', views.BookingFormView.as_view(), name='home'),
    path('booking_list/', views.BookingListView.as_view(), name='BookingListView'),
    path('booking/cancel/<pk>', views.CancelBookingView.as_view(),
         name='CancelBookingView'),
    path('', include('blog.urls')),
#     path('blog/', views.PostList.as_view(), name='blog'),
#     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
#     path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
