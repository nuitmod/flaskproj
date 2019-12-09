import redis
import os, time
#from main_app import *


try:
    r=redis.Redis(host="localhost", port=6379)
    print("redis connected")
except: Exception

def redis_push_data(val):
    r.set('ipy', val)
    redis_value=r.get('ipy'); print(redis_value.decode())
    keys=r.keys('*'); print(keys)
    #key_dict=[k.decode() for k in keys]; print(key_dict)
    #for k in keys: print(k.decode())
