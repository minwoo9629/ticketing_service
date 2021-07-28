from django.contrib import admin
from concertapp.models import Performance, ConcertHall, Seat, Schedule


class SeatAdmin(admin.ModelAdmin):
    list_display = ('concert_hall', 'area', 'number', 'reservation')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('performance', 'concert_hall', 'start_dt', 'end_dt')


admin.site.register(Performance)
admin.site.register(ConcertHall)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Schedule, ScheduleAdmin)
