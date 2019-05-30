from django.views.decorators.cache import cache_page


def url_cache(time_out=30, *args, **kwargs):
    """
    设置缓存，默认缓存时间为30秒，可以直接用到url上而不必每次都写到装饰器内
    """
    return cache_page(time_out, *args, **kwargs)
