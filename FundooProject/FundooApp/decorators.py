from .services import redisCreate
import jwt
import os
from FundooApp import views
def login_user(arg):
    print("in decorator",arg)
    redis_object=redisCreate()
    jwt_token=redis_object.get('token')
    decoded_token=jwt.decode(jwt_token,os.getenv('SECRET_KEY_JWT'))
    user_id=decoded_token['id']
    Notes=views.Note()
    Notes.get(user_id=user_id)
