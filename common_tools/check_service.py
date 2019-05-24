# 检测 memcache rabbitmq redis mysql 服务 是否正常
# pip install python-memcached
# pip install pika
# pip install redis
# pip install PyMySQL
#
import random
import memcache
import pika
import redis
import pymysql

random_str = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
print(random_str)

# 1. memcache-------------------------------------------------------------------------
url = '127.0.0.1:11211'  # 'ip地址：端口'
try:
    mc = memcache.Client([url], debug=0)
    mc.set(random_str, random_str)
    mc.get(random_str)
    print("memcache connect success")
except Exception:
    print("memcache connect error")

# 2.rabbitmq--------------------------------------------------------------------------

ip = 'localhost'  # ip地址
port = '5672'  # 端口
username = 'guest'  # 用户
password = 'guest'  # 密码
try:
    credentials = pika.PlainCredentials(username=username, password=password)
    parameters = pika.ConnectionParameters(host=ip, port=port, credentials=credentials)
    connection = pika.BlockingConnection(parameters=parameters)
    channel = connection.channel()
    channel.queue_declare(queue="hello")
    channel.queue_delete(queue="hello")
    connection.close()
    print("rabbitmq connect success")
except Exception:
    print("rabbitmq connect error")

# 3.redis------------------------------------------------------------------------------

url = 'localhost'  # ip
port = '6379'  # 端口
try:
    pool = redis.ConnectionPool(host=url, port=port, decode_responses=False)
    r = redis.Redis(connection_pool=pool)
    r.set(random_str, random_str)
    r.get(random_str, random_str)
    print("redis connect success")
except Exception:
    print("redis connect error")

# 4.mysql-----------------------------------------------------------------------------
url = '127.0.0.1'  # ip
port = 3306  # 端口
user = 'root'  # 用户
passwd = 'password'  # 密码
db = 'sys'  # 数据库
table = 'sys_config'  # 表
try:
    conn = pymysql.connect(host=url, port=port, user=user, passwd=passwd, db=db, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    effect_row = cursor.execute("select * from {}".format(table))
    row_3 = cursor.fetchall()
    cursor.close()
    conn.close()
    print("mysql connect success")
except Exception:
    print("mysql connect error")
