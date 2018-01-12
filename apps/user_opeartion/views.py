from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from .models import UserFav
from .serializers import UserFavSerializer
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.


class UserFavViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """
    用户收藏
    """
    serializer_class = UserFavSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # authentication_classes = (JSONWebTokenAuthentication, )
    lookup_field = 'goods_id'

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)