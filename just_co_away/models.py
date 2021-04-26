from django.conf import settings
from django.db import models
from django.utils import timezone


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available=True, )

class Listing(models.Model):
    supplier = models.CharField(max_length = 200, default = "N/A")
    available = models.BooleanField()
    price = models.CharField(max_length = 500, default = "N/A")
    phone_number = models.CharField(max_length = 300, default = "N/A")
    landline_number = models.CharField(max_length = 300, default = "N/A")
    whatsapp_number = models.CharField(max_length = 300, default = "N/A")
    address = models.CharField(max_length = 400, default = "N/A")
    state = models.CharField(max_length = 200, default = "N/A")
    city = models.CharField(max_length = 100, default = "N/A")
    pincode = models.CharField(max_length = 100, default = "N/A")
    delivery = models.BooleanField()
    maximum_delivery_distance = models.CharField(max_length = 300, default = "N/A")
    cylinders_per_customer = models.CharField(max_length = 300, default = "N/A")
    date_verified_on = models.DateField()
    verified_on = models.TimeField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    # Model managers
    objects = models.Manager() 
    available_objects = AvailableManager()

    class Meta:
        ordering = ('-date_verified_on','-verified_on')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.supplier
