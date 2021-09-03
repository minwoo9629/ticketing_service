from concertapp.models import Performance, PerformanceSeat, Schedule
from rest_framework.views import APIView
from api.serializers import CategorySerializer
from rest_framework.response import Response


class CategoryListView(APIView):

    def get(self, request, category, format=None):
        start_idx, end_idx = int(request.query_params['start_idx']), int(request.query_params['end_idx'])
        category_list = Performance.objects.filter(category=category)[start_idx:end_idx]
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data)

class RemainTicketCountView(APIView):
    def post(self, request, format=None):
        area = request.POST.get('areaValue')
        date = request.POST.get('date')
        pk = request.POST.get('performanceNumber')
        performance = Performance.objects.get(pk=pk)
        schedule = Schedule.objects.get(performance=performance,start_dt=date)
        remain_seat_count = len(PerformanceSeat.objects.filter(schedule=schedule, seat__area=area, reserved=False))
        context = {'remainCount': remain_seat_count}
        return Response(context)

class GetTicketPrice(APIView):
    def get(self, request, format=None):
        area = request.GET.get('areaValue')
        date = request.GET.get('date')
        pk = request.GET.get('performanceNumber')
        performance = Performance.objects.get(pk=pk)
        schedule = Schedule.objects.get(performance=performance,start_dt=date)
        context = PerformanceSeat.objects.filter(schedule=schedule, seat__area=area).values('price').distinct()[0]
        return Response(context)
