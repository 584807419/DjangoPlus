# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from demo.models import Company
from DjangoPlus.celery import app, MyTask


@app.task(bind=True, base=MyTask)
def add(task_self,name):
    import time
    time.sleep(10)
    res = Company.objects.create(name=name, address='china bj')
    res = dict(res=res.name)
    return res

@app.task(bind=True, base=MyTask)
def big_task(task_self,name):
    import time
    time.sleep(10)
    res = Company.objects.create(name=name, address='china bj')
    res = dict(res=res.name)
    return res


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
