from concertapp.models import Performance
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
        remain_seat_count = len(performance.schedule.get(start_dt=date).concert_hall.seats.filter(area=area, reservation=False))

        context = {'remainCount': remain_seat_count}
        return Response(context)