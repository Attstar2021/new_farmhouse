from django.contrib import admin
from .models import RoomCategory, Room, Booking, Guest

# Register your models here.
admin.site.register(RoomCategory)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Guest)