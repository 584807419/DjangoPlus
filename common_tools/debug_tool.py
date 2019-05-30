import traceback
import logging
import pysnooper

LOG = logging.getLogger('error_log')

from rest_framework.response import Response


def trace_execption(func):
    """
    1.当settings里面设置DEBUG为True的时候可以方便的查看异常调用栈信息，但是FALSE的时候看不到
    2.错误发生要记录或者知道，但是不影响一次请求主流程的完成
    这两种情况，可以套这个装饰器拿到异常信息的详细内容，方便排查和定位异常代码位置
    """

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            error_msg = traceback.format_exc()
            LOG.error(error_msg)
            return Response({"error_msg": error_msg})

    return wrapper
