from django.db import models
from django.conf import settings
from django.urls import reverse_lazy

# Create your models here.


class RoomCategory(models.Model):
    category = models.CharField(max_length=50)
    rate = models.FloatField()

    def __str__(self):
        return self.category


class Room(models.Model):
    number = models.IntegerField()
    beds = models.IntegerField()
    capacity = models.IntegerField()
    category = models.ForeignKey(
        RoomCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.number}. Beds = {self.beds} Person = {self.capacity}'


class Booking(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    
    def __str__(self):
        return f'From = {self.check_in.strftime("%d-%b-%Y %H:%M")} To = {self.check_out.strftime("%d-%b-%Y %H:%M")}'

    def get_cancel_booking_url(self):
        return reverse_lazy('home:CancelBookingView', args=[self.pk, ])

class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
