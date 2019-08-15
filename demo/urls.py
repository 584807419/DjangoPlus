from django.conf.urls import url
from demo import views
urlpatterns = [

    url(r'top/free/(?P<id>[0-9]+)/$', views.get_test),
]
