from .models import Goods
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import GoodsSerializer
# Create your views here.


class GoodsListView(APIView):
    """
    商品列表页
    """

    def get(self, request):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    def post(self, request):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)