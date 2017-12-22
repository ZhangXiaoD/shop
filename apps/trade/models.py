from django.db import models

from users.models import UserProfile
from goods.models import Goods

# Create your models here.


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    goods = models.ForeignKey(Goods, verbose_name='商品')
    goods_num = models.IntegerField(default=0, verbose_name='商品数量')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}({})'.format(self.goods.name, self.goods_num)


class OrderInfo(models.Model):
    """
    订单
    """
    ORDER_STATUS = (
        ('success', '成功'),
        ('cancel', '取消'),
        ('await_pay', '待支付')
    )
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    order_sn = models.CharField(max_length=30, unique=True, verbose_name='订单号')
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name='支付平台返回单号')
    pay_status = models.CharField(choices=ORDER_STATUS, max_length=20, verbose_name='订单状态')
    post_script = models.CharField(max_length=200, verbose_name='订单留言')
    order_mount = models.FloatField(default=0.0, verbose_name='订单金额')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间')
    # 用户信息
    address = models.CharField(max_length=100, default='', verbose_name='收货地址')
    sign_name = models.CharField(max_length=20, default='', verbose_name='签收人')
    sign_mobile = models.CharField(max_length=11, verbose_name='联系电话')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_sn


class OrderGoods(models.Model):
    """
    订单的商品详情
    """
    order = models.ForeignKey(OrderInfo, verbose_name='订单')
    goods = models.ForeignKey(Goods, verbose_name='商品')
    goods_num = models.IntegerField(default=0 ,verbose_name='商品数量')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '订单的商品详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.order_sn