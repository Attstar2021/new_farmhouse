from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, FormView, View, DeleteView
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Room, Booking, RoomCategory
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import render, redirect
from .forms import BookingForm

#class BookingFormView(View):
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BookingListView')
    form = BookingForm()
    context = {
        'form': form 
    }
    return render(request, 'home.html', context)
    




   
class BookingListView(ListView):
    model = Booking
    template_name = "booking_list.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user.id)
            return booking_list



def delete_booking(request, booking_id):
    context = {}
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        booking.delete()
        return HttpResponseRedirect("/")

    return render(request, "cancel_booking_view.html", context)

# class CancelBookingView(DeleteView):
#     model = Booking
#     template_name = 'cancel_booking_view.html'
#     success_url = reverse_lazy('BookingListView')



	