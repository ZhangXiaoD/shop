import random

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from .models import UserProfile, VerifyCode
from .serializers import SmsSerializer, RegisterSerializer, UserDetailSerializer

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


class SmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
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



class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    用户注册
    """
    queryset = UserProfile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # if serializer.validated_data['type'] != 1:
        #     return Response({'status':1, 'msg': '注册失败'})
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        if self.action == 'create':
            return []
        return []

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return RegisterSerializer
        return UserDetailSerializer