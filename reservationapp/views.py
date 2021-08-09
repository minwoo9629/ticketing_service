from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from concertapp.models import Performance
# Create your views here.

@login_required
def reserve(request, pk):
    performance = Performance.objects.filter(id=pk)
    context = {
        'performance':performance,
    }
    return render(request, 'reservationapp/reserve.html', context)