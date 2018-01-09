import random

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from .models import UserProfile, VerifyCode
from .serializers import SmsSerializer, RegisterSerializer

# Create your views here.


class CustomBackend(ModelBackend):
    """
    自定义用户认证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成6位数字验证码
        :return:
        """
        seeds = '1234567890'
        random_str = []
        for i in range(6):
            random_str.append(random.choice(seeds))
        return ''.join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']
        code = self.generate_code()

        code_record = VerifyCode(code=code, mobile=mobile)
        code_record.save()
        return Response({'status': 0, 'msg': '发送验证码成功。'})


class UserViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    用户注册
    """
    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer