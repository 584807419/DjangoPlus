from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from demo.models import Company
from DjangoPlus.celery import app, MyTask
from demo.tasks import add, big_task


# Create your views here.

class Demo(APIView):
    def get(self, request):
        big_task.delay('zhangkun')
        return Response({"success": 'ali'})
