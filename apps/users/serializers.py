import re
import datetime
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from shop.settings import REGEX_MOBILE
from .models import UserProfile, VerifyCode


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """
        # 手机是否注册
        if UserProfile.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('用户已经存在')
        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError('手机号码非法')
        # 验证发送频率
        one_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=1)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile).count():
            raise serializers.ValidationError('距离上次发送未超过60秒')
        return mobile


class RegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(min_length=6, max_length=6, write_only=True,
                                 help_text='验证码',
                                 error_messages={
                                     'required': '请输入验证码',
                                     'min_length': '验证码格式错误',
                                     'max_length': '验证码格式错误'
                                 })
    username = serializers.CharField(min_length=6, max_length=20,
                                     validators=[UniqueValidator(queryset=UserProfile.objects.all(),
                                                                 message='该用户名已存在')])
    password = serializers.CharField(min_length=6, max_length=20, write_only=True,
                                     style={'input_type': 'password'})
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_code(self, code):
        verify_record = VerifyCode.objects.filter(mobile=self.initial_data['mobile']).order_by('-add_time')
        if verify_record:
            last_record = verify_record[0]
            five_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=5)
            # 验证码时间验证
            if last_record.add_time < five_minutes_ago:
                raise serializers.ValidationError('验证码过期')
            # 验证码验证
            if last_record.code != code:
                raise serializers.ValidationError('验证码错误')
        else:
            raise serializers.ValidationError('验证码错误')

    def validate(self, attrs):
        del attrs['code']
        return attrs

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'code', 'mobile', 'password')


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    mobile = serializers.CharField(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('name', 'gender', 'birthday', 'email', 'mobile')