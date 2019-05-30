from django.shortcuts import render
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response
from demo.models import Company
from DjangoPlus.celery import app, MyTask
from demo.tasks import add, big_task
from common_tools.debug_tool import trace_execption
import logging
import pysnooper

LOG = logging.getLogger('error_log')  # 拿到logger对象


# Create your views here.

class Demo(APIView):
    @trace_execption
    def get(self, request):
        # a = 9 / 0
        # big_task.delay('zhangkun')
        # res = Company.objects.all()

        from common_tools.email_tool import send_email
        send_email('测试', '张昆', to_address='qq.com')
        return Response({"success": 'ali'})

import pysnooper
class Demo1(APIView):
    @pysnooper.snoop()
    def get(self, request):
        a = 9
        b = 8
        c = 'zhangkun'
        return Response({"success": 'ali'})

import pysnooper
class Demo2(APIView):
    def get(self, request):
        import time
        return Response({"success": time.time()})