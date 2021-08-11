from concertapp.models import Performance
from reservationapp.models import Reservation
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
        reserved_seat_count = len(Reservation.objects.filter(schedule__performance=performance,schedule__start_dt=date,seat__area=area, user=None))
        remain_seat_count = reserved_seat_count

        context = {'remainCount': remain_seat_count}
        return Response(context)