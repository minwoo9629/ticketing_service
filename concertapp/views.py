from django.shortcuts import render
from concertapp.models import Performance
from django.views.generic import DetailView, ListView
from django.utils import timezone

def performance_list_view(request):
    current_date = timezone.now().strftime('%Y-%m-%d')
    now_playing =  Performance.objects.filter(ticket_open_dt__lte=current_date).order_by('ticket_open_dt')[:6]
    comming_soon = Performance.objects.filter(ticket_open_dt__gte=current_date).order_by('ticket_open_dt')[:5]
    advertisement = Performance.objects.filter(advertisement=True)
    
    context = {'now_playing':now_playing, 'comming_soon': comming_soon, 'advertisement': advertisement}
    return render(request, 'concertapp/list.html', context)


class CategoryListView(ListView):
    model = Performance
    template_name = 'concertapp/category.html'
    context_object_name = 'performance_category_list'

    def get_queryset(self, *args, **kwargs):
        concert_list = Performance.objects.filter(category=self.kwargs.get('category'))
        return concert_list

class PerformanceDetailView(DetailView):
    model = Performance
    template_name = 'concertapp/detail.html'
    context_object_name = 'performance'