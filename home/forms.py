from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'room', 'check_in', 'check_out']
    
        widgets = {
                'check_in': forms.DateInput(attrs={'type': 'date'}),
                'check_out': forms.DateInput(attrs={'type': 'date'}),
            }
    
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

        import datetime
        # Get today's date
        today = datetime.date.today()

        # Set the min attribute to today's date for both date fields
        self.fields['check_in'].widget.attrs['min'] = today
        self.fields['check_out'].widget.attrs['min'] = today
