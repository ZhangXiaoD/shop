import xadmin
from .models import Goods, GoodsImage, Banner


class GoodsAdmin(object):
    list_display = ['category', 'goods_sn', 'name', 'add_time']
    search_fields = ['category', 'goods_sn', 'name']
    list_filter = ['category', 'goods_sn', 'name', 'add_time']


class GoodsImageAdmin(object):
    list_display = ['goods', 'image', 'add_time']
    search_fields = ['goods', 'image']
    list_filter = ['goods', 'image', 'add_time']


class BannerAdmin(object):
    list_display = ['goods', 'image', 'index', 'add_time']
    search_fields = ['goods', 'image', 'index']
    list_filter = ['goods', 'image', 'index', 'add_time']


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(Banner, BannerAdmin)