from django.shortcuts import render
from concertapp.models import Performance
from django.views.generic import DetailView, ListView
from django.utils import timezone
from django.db.models import Q


def performance_list_view(request):
    current_date = timezone.now().strftime('%Y-%m-%d')
    now_playing = Performance.objects.filter(ticket_open_dt__lte=current_date).order_by('ticket_open_dt')[:6]
    comming_soon = Performance.objects.filter(ticket_open_dt__gte=current_date).order_by('ticket_open_dt')[:5]
    advertisement = Performance.objects.filter(advertisement=True)

    context = {'now_playing': now_playing, 'comming_soon': comming_soon, 'advertisement': advertisement}
    return render(request, 'concertapp/list.html', context)


class CategoryListView(ListView):
    model = Performance
    template_name = 'concertapp/category.html'
    context_object_name = 'performance_category_list'

    def get_queryset(self, *args, **kwargs):
        concert_list = Performance.objects.filter(category=self.kwargs.get('category'))[:12]
        return concert_list


class PerformanceDetailView(DetailView):
    model = Performance
    template_name = 'concertapp/detail.html'
    context_object_name = 'performance'


class SearchListView(ListView):
    model = Performance
    template_name = 'concertapp/search.html'
    context_object_name = 'search_list'
    paginate_by = 10
    block_size = 5
    
    def get_queryset(self, *args, **kwargs):
        q = self.request.GET.get('q', '')
        start_day = self.request.GET.get('start_day', None)
        end_day = self.request.GET.get('end_day', None)

        search_list = Performance.objects.filter(title__contains=q)
        if start_day is not None:
            search_list = search_list.filter(~Q(start_day__gt=end_day) & ~Q(end_day__lt=start_day))
        
        return search_list

    def get_context_data(self, *, object_list=None, **kwargs):
        q = self.request.GET.get('q', '')
        start_day = self.request.GET.get('start_day', '')
        end_day = self.request.GET.get('end_day', '')

        context = super(SearchListView, self).get_context_data()
        start_idx = (context['page_obj'].number -1 ) // self.block_size * self.block_size
        end_idx = min(start_idx + self.block_size, len(context['paginator'].page_range))
        context['page_range'] = context['paginator'].page_range[start_idx:end_idx]
        context['keyword'] = q
        context['start_day'] = start_day
        context['end_day'] = end_day

        return context
        