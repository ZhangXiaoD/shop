from .models import Goods, GoodsCategory
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework.backends import DjangoFilterBackend

from .serializers import GoodsSerializer, CategorySerializer
from .filters import GoodsFilter
from .paginations import GoodsPagination
# Create your views here.


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # authentication_classes = (JSONWebTokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
    pagination_class = GoodsPagination
    # authentication_classes = (JSONWebTokenAuthentication, )
