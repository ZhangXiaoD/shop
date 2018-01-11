from rest_framework import viewsets
from rest_framework import mixins

from .models import UserFav
from .serializers import UserFavSerializer

# Create your views here.


class UserFavViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    用户收藏
    """
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer