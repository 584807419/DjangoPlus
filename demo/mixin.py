import time
import datetime
import random


class QueryTest:
    temp_dict = dict()
    temp_dict[time.time()] = time.time()
    temp_dict[random.randint(0,100)] = datetime.datetime.now()
