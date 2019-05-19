from django.urls import path
from demo.views import Demo

urlpatterns = [
    path('get_test/', Demo.as_view())
]
