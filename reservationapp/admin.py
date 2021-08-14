from django.contrib import admin
from reservationapp.models import Ticket, Reservation

class TicketAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['user']}),
        ("information", {'fields':['schedule', 'seat'], 'classes':['collapse']}),
    ]
    # list_display = ['user', 'schedule', 'seat']


class ReservationAdmin(admin.ModelAdmin):
    list_display =  ('user','id','reserve_date')

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Reservation, ReservationAdmin)
# Register your models here.

