from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, FormView, View, DeleteView
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from home.booking_logic.form import AvailabilityForm
from .models import Room, Booking, RoomCategory
from home.booking_logic.availability import check_availability
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
class BookingFormView(View):
    
    model = Booking
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if "check_in" in request.session:
            s = request.session
            form_data = {
                "check_in": s['check_in'], "check_out": s['check_out'], "room_category": s['room_category']}
            form = AvailabilityForm(request.POST or None, initial=form_data)
        else:
            form = AvailabilityForm()
        return render(request, 'home.html', {'form': form})
        

    def post(self, request, *args, **kwargs):
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data


            request.session['check_in'] = data['check_in'].strftime(
                "%Y-%m-%dT%H:%M")
            request.session['check_out'] = data['check_out'].strftime(
                "%Y-%m-%dT%H:%M")
            request.session['room_category'] = data['room_category'].category
            return redirect('home')
            return redirect('RoomDetailView')
        return HttpResponse('form not valid')



class BookingListView(ListView):
    model = Booking
    template_name = "booking_list_view.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user.id)
            return booking_list



class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'cancel_booking_view.html'
    success_url = reverse_lazy('BookingListView')