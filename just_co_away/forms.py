from django import forms

from .models import Listing

class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ('supplier', 'available', 'price', 'phone_number', 'landline_number', 'whatsapp_number', 'address', 'state', 'city', 'pincode', 'delivery', 'maximum_delivery_distance', 'cylinders_per_customer','date_verified_on', 'verified_on')

        widgets = {
        'verified_on' : forms.TimeInput(attrs={'type':'time'}, format='%H:%M:'),
        'date_verified_on': forms.DateInput(attrs={'type':'date'}, format='%m/%d/%Y'),
        
        }