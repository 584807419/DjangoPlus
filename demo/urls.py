from django.conf.urls import include, url
from demo.views import Demo

urlpatterns = [
    url(r'^get_test/', Demo.as_view())
]
