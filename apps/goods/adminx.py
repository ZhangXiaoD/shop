import xadmin
from .models import Goods, GoodsImage, Banner, GoodsCategory, GoodsCategoryBrand


class GoodsCategoryAdmin(object):
    list_display = ['name', 'code', 'desc', 'category_type', 'parent_category', 'is_tab', 'add_time']
    search_fields = ['name', 'code', 'desc', 'category_type', 'parent_category', 'is_tab']
    list_filter = ['name', 'code', 'desc', 'category_type', 'parent_category', 'is_tab', 'add_time']


class GoodsCategoryBrandAdmin(object):
    list_display = ['name', 'image', 'add_time']
    search_fields = ['name', 'image']
    list_filter = ['name', 'image', 'add_time']


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


xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsCategoryBrandAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(Banner, BannerAdmin)