import redis
import os


def redis_config():
    try:
        return redis.Redis(host=os.environ.get("REDIS_HOST"),
                           port=os.environ.get("REDIS_PORT"),
                           db=os.environ.get("REDIS_DATABASE"))
    except (Exception,):
        print("redis connection failure")
