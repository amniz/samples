import redis

r = redis.Redis(
    host='localhost',
    port='6379', )


class redisCreate:
    # method to set the redis key value
    def set(self, key, value):
        try:
            r.set(key, value)  # setting the key value in redis cache
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)

    # method to get redis key value
    def get(self, key):
        try:
            key = r.get(key)  # returning the redis key value
            return key
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
