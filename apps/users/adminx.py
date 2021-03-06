import xadmin
from .models import VerifyCode


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', 'add_time']
    search_fields = ['code', 'mobile']
    list_filter = ['code', 'mobile', 'add_time']


xadmin.site.register(VerifyCode, VerifyCodeAdmin)