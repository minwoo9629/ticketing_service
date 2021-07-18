from django.shortcuts import render
from concertapp.models import Performance
from django.views.generic import DetailView


def performance_list_view(request):
    now_playing = Performance.objects.all()[:6]
    comming_soon = Performance.objects.all()[6:12]
    context = {'now_playing':now_playing, 'comming_soon': comming_soon}
    return render(request, 'concertapp/list.html', context)


def concert_list_view(request):
    return render(request, 'concertapp/conert.html')



class PerformanceDetailView(DetailView):
    model = Performance
    template_name = 'concertapp/detail.html'
    context_object_name = 'performance'
    
# def performance_detail_view(request, pk):
#     performance = Performance.objects.get(pk=pk)
#     return render(request, 'concertapp/detail.html', context)