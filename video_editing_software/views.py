# import requests
# import json
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.utils.decorators import method_decorator
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from demo.models import Company
# from DjangoPlus.celery import app, MyTask
# from demo.tasks import add, big_task
# from common_tools.debug_tool import trace_execption
# from demo.mixin import QueryTest
# import logging
# import pysnooper
#
# LOG = logging.getLogger('error_log')  # 拿到logger对象
#
#
# # Create your views here.
#
# class Demo(APIView):
#     @trace_execption
#     def get(self, request):
#         # a = 9 / 0
#         # big_task.delay('zhangkun')
#         # res = Company.objects.all()
#
#         from common_tools.email_tool import send_email
#         send_email('测试', '张昆', to_address='qq.com')
#         return Response({"success": 'ali'})
#
#
# import pysnooper
#
#
# class Demo1(APIView):
#     @pysnooper.snoop()
#     def get(self, request):
#         a = 9
#         b = 8
#         c = 'zhangkun'
#         return Response({"success": 'ali'})
#
#
# class Demo2(APIView):
#     def get(self, request):
#         import time
#         from .models import Company
#         aa = Company.objects.all()
#         return Response({"success": time.time(), 'aa': aa[0].name})
#
#
# class Demo3(APIView, QueryTest):
#     def get(self, request):
#         self.temp_dict[id(request)] = id(request)
#         return Response(self.temp_dict)
#
#
# def get_test(request, id):
#         temp_dict = dict()
#         res = requests.get('https://rss.itunes.apple.com/api/v1/us/ios-apps/top-free/all/100/explicit.json')
#         res_json = json.loads(res.content)
#         for k, v in enumerate(res_json.get('feed').get('results')):
#             if k + 1 == int(id):
#                 temp_dict[v.get('name')] = v.get('artworkUrl100')
#         return JsonResponse(temp_dict)
#
# from django.http import HttpResponse
# from django.views.generic import ListView, DetailView
# from video_editing_software.models import VideoEditSoftware
#
#
# class VideoEditingSoftwareList(ListView):
#     model = VideoEditSoftware
#
# class VideoEditingSoftwareDetail(DetailView):
#     model = VideoEditSoftware
