from django.urls import path
from demo.views import Demo
from demo.views import Demo1
from demo.views import Demo2
from common_tools.cache_tool import url_cache

urlpatterns = [
    path('get_test/', Demo.as_view()),
    path('get_test1/', Demo1.as_view()),
    path('get_test2/', url_cache()(Demo2.as_view()))  # 缓存的使用
]
