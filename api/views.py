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





