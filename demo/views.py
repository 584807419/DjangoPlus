from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from demo.models import Company
from DjangoPlus.celery import app, MyTask
from demo.tasks import add, big_task
from common_tools.debug_tool import trace_execption
import logging

LOG = logging.getLogger('error_log') # 拿到logger对象


# Create your views here.

class Demo(APIView):
    @trace_execption
    def get(self, request):
        a = 9/0
        # big_task.delay('zhangkun')
        res = Company.objects.all()
        LOG.info('666666666666666info')
        LOG.warning('6666666666666666warn')
        LOG.error('666666666666666666error')
        LOG.error('res:{}'.format(res))
        return Response({"success": 'ali'})
