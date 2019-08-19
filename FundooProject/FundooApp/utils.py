from . import services
import redis
import jwt

# def getuser(token):
#     decoded_token=jwt.decode(token)
#     print(decoded_token)


    # r = redis.StrictRedis(host='localhost', port=6379, db=0)
    # for key in r.scan_iter("user:*"):
    #     m=r.get(key)
    #     print('m',m)
    # # return m
