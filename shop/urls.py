"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import xadmin
from shop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewSet, IndexCategoryViewSet
from users.views import SmsCodeViewSet, UserViewSet
from user_opeartion.views import UserFavViewSet, LeavingMessageViewSet, AddressViewSet
from trade.views import ShoppingCartViewSet, OrderViewSet

router = DefaultRouter()
# 配置goods的url
router.register('goods', GoodsListViewSet, base_name='goods')
# 配置category的url
router.register('categorys', CategoryViewSet, base_name='categorys')
# 配置发送验证码url
router.register('send_code', SmsCodeViewSet, base_name='send_code')
# 配置用户url
router.register('users', UserViewSet, base_name='users')
# 配置用户收藏url
router.register('userfavs', UserFavViewSet, base_name='userfavs')
# 配置留言url
router.register('message', LeavingMessageViewSet, base_name='message')
# 配置收货地址url
router.register('address', AddressViewSet, base_name='address')
# 配置购物车url
router.register(('shopcards'), ShoppingCartViewSet, base_name='shopcards')
# 配置订单url
router.register(('order'), OrderViewSet, base_name='order'),
# 配置轮播图url
router.register(('banner'), BannerViewSet, base_name='banner')
# 配置首页商品分类数据url
router.register(('indexgoods'), IndexCategoryViewSet, base_name='indexgoods')



urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/', obtain_jwt_token),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url(r'^doc/', include_docs_urls(title='shop')),


    url(r'^', include(router.urls)),


]
