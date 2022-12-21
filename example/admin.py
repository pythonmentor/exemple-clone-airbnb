from django.contrib import admin

from .models import Reservation, Accommodation, Availability

admin.site.register(Reservation)
admin.site.register(Accommodation)
admin.site.register(Availability)
