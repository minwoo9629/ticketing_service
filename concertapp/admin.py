from django.contrib import admin
from concertapp.models import Performance, ConcertHall, Seat, Schedule, Description


class SeatAdmin(admin.ModelAdmin):
    list_display = ('concert_hall', 'floor', 'area', 'row', 'number', 'reservation')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('performance', 'concert_hall', 'start_dt', 'end_dt')

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('performance','description')

admin.site.register(Performance)
admin.site.register(ConcertHall)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Description, DescriptionAdmin)
