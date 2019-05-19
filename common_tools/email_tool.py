from django.core.mail import send_mail


def send_email(title, msg, to_address=['584807419@qq.com', ]):
    """
    简单封装 用法send_email('测试', '张昆',to_address=['qq.com','aa.com'])
    :param title: str
    :param msg: str
    :param to_address: list or tuple
    :return: 成功 返回 1
    """
    res = send_mail(title, msg, 'send from Django plus', to_address)
    print(res)
    return res
