from django.http import HttpResponse

from django_redis import get_redis_connection

conn_redis = get_redis_connection()


def use_string(request):
    conn_redis.set('me_string', 'zhangkun')
    conn_redis.hset('me_hash', 'name', 'zhangkun')
    conn_redis.rpush('me_list', 'zhangkun')
    conn_redis.sadd('me_set', 'zhangkun')
    conn_redis.zadd('me_sorted_set', {'zhangkun':1})
    res = {
        'me_string': conn_redis.get('me_string'),
        'me_hash': conn_redis.hget('me_hash','name'),
        'me_list': conn_redis.rpop('me_list'),
        'me_set': conn_redis.spop('me_set'),
        'me_list': conn_redis.zrange('me_sorted_set',0,100),
    }
    print(res)
    return HttpResponse([res])
