from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav


class UserFavSerializer(serializers.ModelSerializer):
    """
    用户收藏商品序列化
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message='已经收藏'
            )
        ]
        fields = ('id', 'user', 'goods')