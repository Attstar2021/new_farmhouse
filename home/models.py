from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here
class RoomCategory(models.Model):
    category = models.CharField(max_length=50)
    #rate = models.FloatField()

    def __str__(self):
        return self.category


class Room(models.Model):
    number = models.IntegerField()
    beds = models.IntegerField()
    capacity = models.IntegerField()
    category = models.ForeignKey(
        RoomCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} bed for {self.capacity} people'


class Booking(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    #slug = models.SlugField(max_length=200, unique=True, null=True)
    
    def __str__(self) -> str:
        return f' Hotel has been booked From = {self.check_in.strftime("%d-%b-%Y")} To = {self.check_out.strftime("%d-%b-%Y")}'

    # def save(self, *args, **kwargs):
    #     # Generate slug when saving the object
    #     self.slug = slugify(self.hotel_name)
    #     super().save(*args, **kwargs)

    #def get_absolute_url(self):
       # return reverse('BookingListView', args=[str(self.slug)])
