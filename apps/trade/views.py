from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions

from utils.permissions import IsOwnerOrReadOnly
from .serializers import ShoppingCartSerializer, ShoppingCartDetailSerializer, OrderSerializer
from .models import ShoppingCart, OrderInfo, OrderGoods
# Create your views here.


class ShoppingCartViewSet(viewsets.ModelViewSet):
    """
    list:
        获取购物车详情
    create:
        加入购物车
    delete:
        删除购物记录
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    lookup_field = 'goods_id'

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ShoppingCartDetailSerializer
        else:
            return ShoppingCartSerializer


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    create:
        新增订单
    delete:
        删除订单
    list:
        获取订单
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = OrderSerializer

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        order = serializer.save()
        shop_carts = ShoppingCart.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            order_goods = OrderGoods()
            order_goods.goods = shop_cart.goods
            order_goods.goods_num = shop_cart.nums
            order_goods.order = order
            order_goods.save()

            shop_cart.delete()
        return order