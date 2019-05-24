from django.urls import path
from demo.views import Demo
from demo.views import Demo1

urlpatterns = [
    path('get_test/', Demo.as_view()),
    path('get_test1/', Demo1.as_view())
]
