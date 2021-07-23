from django.shortcuts import render
from concertapp.models import Performance
from django.views.generic import DetailView
from django.utils import timezone

def performance_list_view(request):
    current_date = timezone.now().strftime('%Y-%m-%d')
    now_playing =  Performance.objects.filter(ticket_open_dt__lte=current_date).order_by('ticket_open_dt')[:5]
    comming_soon = Performance.objects.filter(ticket_open_dt__gte=current_date).order_by('ticket_open_dt')[:5]
    advertisement = Performance.objects.filter(advertisement=True)
    
    context = {'now_playing':now_playing, 'comming_soon': comming_soon, 'advertisement': advertisement}
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