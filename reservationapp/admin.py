from django.contrib import admin
from reservationapp.models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['user']}),
        ("information", {'fields':['schedule', 'seat'], 'classes':['collapse']}),
    ]
    # list_display = ['user', 'schedule', 'seat']

admin.site.register(Reservation, ReservationAdmin)
# Register your models here.

