import redis
try:
    r = redis.StrictRedis(host='localhost',

                                port=6379,

                                db=0)
except Exception as e:
    print(e)

class redisCreate:
    # method to set the redis key value
    def set(self, key, value):
        try:
            r.set(key, value)  # setting the key value in redis cache
        except ValueError as e:
            return e
        except KeyError as e:
            return e

    # method to get redis key value
    def get(self, key):
        try:
            data = r.get(key)  # returning the redis key value
            return data
        except ValueError as e:
            return e
        except KeyError as e:
            return e

    # method to remove the redis token or key
    def remove(self, key):
        try:
            r.delete(key)  # deleting the key
        except KeyError as e:
            return e
        except ValueError as e:
            return e

    def hset(self,coment,key,value):
        r.hset(coment,key,value)

    def getall(self,para):
        return r.hgetall(para)
