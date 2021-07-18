from django.shortcuts import render
from concertapp.models import Performance


def concert_list_view(request):
    now_playing = Performance.objects.all()[:6]
    comming_soon = Performance.objects.all()[6:12]
    context = {'now_playing':now_playing, 'comming_soon': comming_soon}
    return render(request, 'concertapp/list.html', context)
