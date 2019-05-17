import os
import celery

from kombu import Queue, Exchange
from celery import platforms, Celery
from django.conf import settings

platforms.C_FORCE_ROOT = True  # 解决celery不能用root用户启动问题

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoPlus.settings')  # 设置依赖的环境变量

app = Celery('DjnagoPlus_Celery_Task', broker=settings.CELERY_CONFIG_DETAIL_DICT.get('CELERY_BROKER_URL'))
# 创建一个celery类的对象

app.autodiscover_tasks()  # 自动检索每个app下的tasks.py


class MyRouter(object):
    """
    设置路由，对指定的任务名，指定对应的队列和routing_key
    """

    @staticmethod
    def route_for_task(task, *args, **kwargs):
        if 'big_task' in task:
            # 名字里面带big_task的任务消，设置routing_key为big_task，进到big_task队列
            return {
                'queue': 'big_task',
                'exchange': 'big_task',
                'routing_key': 'big_task',
                'exchange_type': 'topic'
            }
        elif 'small_task' in task:
            return {
                'queue': 'small_task',
                'exchange': 'small_task',
                'routing_key': 'small_task',
                'exchange_type': 'topic'
            }
        else:
            return {
                'queue': 'default',
                'exchange': 'default',
                'routing_key': 'default',
                'exchange_type': 'topic'
            }


class MyTask(celery.Task):
    """
    不用filter=task_method时，实例(self)不会自动传入。
    只有bind=True时， task对象会作为第一个参数自动传入。
    加上filter=task_method参数，实例(self)会作为第一个参数自动传入。
    加上filter=task_method, bind=True, task对象会作为第一个，实例(self)会作为第二个参数自动传入。

    定义异步任务:
    from celery.contrib.methods import task_method
    class A(object):
        def __init__(self):
            object.__init__(self)
            self.a = 1
            self.b = 2

        @app.task(bind=True, filter=task_method, base=MyTask)
        def test1(task_self, self, a, b):
            try:
                print a
                print b
                return a+b+self.a+self.b
            except Exception as e:
                # 调用了retry它会发送一个新的消息，使用相同的任务id，会确保消息被送到和原来的任务相同的队列中
                raise task_self.retry(exc=exc)
                # 在调用了retry后会引发Retry异常，这将终止其后的代码执行，可以在调用时附带throw=False不抛出异常，exc带的是异常信息

    调用异步任务:
    a = A()
    result = a.test1.delay(4, 4)
    # delay 返回的是一个 AsyncResult 对象，里面存的就是一个异步的结果，当任务完成时result.ready() 为 true，然后用 result.get() 取结果即可
    """

    def on_success(self, retval, task_id, args, kwargs):
        """在任务执行成功时调用"""
        print("异步任务执行成功 返回值信息:{}".format(retval))
        return super(MyTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """
        在任务失败时调用
        """
        print("异步任务执行异常 错误信息:{}".format(exc))
        return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)


app.conf.update(**settings.CELERY_CONFIG_DETAIL_DICT, CELERY_ROUTES=(MyRouter(),))

# mac上面开启rabbitmq
# cd /usr/local/Cellar/rabbitmq/3.7.9/sbin
# rabbitmq-server
# http://localhost:15672/  guest/guest 可可视化查看队列状态

# celery worker
# 开启一个worker 用 celery -A DjangoPlus worker -l info 命令开启，即可工作