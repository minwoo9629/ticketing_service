from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from concertapp.models import Performance, Schedule, Seat
# Create your views here.

@login_required
def reserve(request, pk):
    # performance = Performance.objects.get(id=pk)
    schedule = Schedule.objects.filter(performance=pk)
    seats = Seat.objects.filter(concert_hall=schedule[0].concert_hall)
    context = {
        # 'performance':performance,
        'schedule':schedule,
        'seats':seats,
    }
    return render(request, 'reservationapp/reserve.html', context)