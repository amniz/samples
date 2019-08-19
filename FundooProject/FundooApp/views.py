#####################################################################################################################
# @author:Muhammed Nisamudheen
# version :{
#               python 3.6
#               django: 2.2
# }
# purpose : Fundoo Application
######################################################################################################################
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import jwt
from rest_framework.views import APIView
from . import services
from .Serializers import CreateUserSerializer
import os
from . import utils
from .services import redisCreate
from dotenv import load_dotenv, find_dotenv
from pathlib import *

load_dotenv(find_dotenv())
env_path = Path('.') / '.env'
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import FundooNotes
from .Serializers import NoteSerializer
import django_redis
import logging
import boto3
from botocore.exceptions import ClientError
from django.contrib.auth.models import User
from .decorators import login_user

@api_view(["GET"])
def loginsocial(request):
    return render(request, 'FundooApp/login.html')


def success(request):
    return render(request, 'FundooApp/success.html')


# Create your views here.
# activate view key purpose is to activate the user account using the generated token
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def activate(request, token):
    payload = jwt.decode(token, os.getenv('SECRET_KEY_JWT'))  # decoding the payload from the jwt token
    email = payload['email']  # getting email from the pay load
    userid = payload['userid']  # getting the user id from the payload
    msg = {'Error': "Token mismatch", 'status': "401"}
    try:
        serializer_object = CreateUserSerializer()  # creating a serializer object
        serializer_object.validate(userid, email)  # calling the validate method in the serializer
        return Response({'message': 'successful'})
    except Exception:
        return Response({'message': 'invalid data'})


# method to register or signup for the new user with the valid details
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    serializer_object = CreateUserSerializer()  # creating serializer object
    try:
        if request.POST.get("username") is None:
            raise ValueError("username field required")
        elif request.POST.get("firstname") is None:
            raise ValueError("firstname field required")
        elif request.POST.get("lastname") is None:
            raise ValueError("lastname field required")
        elif request.POST.get("email") is None:
            raise ValueError("email field required")
        elif request.data.get("password") is None:
            raise ValueError("password field required")
    except Exception as error:
        return Response({'Caught this error: ' + repr(error)})
    serializer = CreateUserSerializer.create(serializer_object, validated_data=request.data)  # calling the create
    # method to insert data in the User model
    current_site = get_current_site(request)  # getting the current domain address
    mail_subject = 'Activate your account.'  # subject of the mail
    try:
        payload = {  # payload to be in included in the token
            'email': serializer.email,
            'username': serializer.username,
            'userid': serializer.id

        }
    except Exception:
        return Response({"message": "duplicate email not allowed"})

    token = jwt.encode(payload, os.getenv('SECRET_KEY_JWT'), algorithm='HS256').decode('utf-8')  # generating the token
    message = render_to_string('FundooApp/account_active_email.html', {
        'domain': current_site.domain,
        'token': token,
    })  # generating the message to be send with the email ,rendering the link to account_active_email and giving
    # payload in url
    to_email = serializer.email  # getting the email address
    email = EmailMessage(
        mail_subject, message, to=[to_email]  # creating object of EmailMessage class
    )
    email.send()  # sending the email
    return HttpResponse('Please confirm your email address to complete the registration')


# method used for login of the user by providing username and password
@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes((AllowAny,))
def login(request):  # allows the user for login
    username = request.POST.get("username")  # getting the user name
    password = request.POST.get("password")  # getting the password
    if username is None or password is None:  # validating whether any of the data is none or not
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)  # verifying the user name and password
    if not user:
        return Response({'error': 'Invalid Credentials'},  # if not found returning
                        status=HTTP_404_NOT_FOUND)
    payload = {
        'id': user.id,
        'username': user.username  # generating payload

    }
    encoded_jwt = jwt.encode(payload, os.getenv('SECRET_KEY_JWT'), algorithm='HS256')  # generating the token
    redis_key = redisCreate()  # creating the redis object
    redis_key.set('token', encoded_jwt)  # setting the redis cache key
    return Response({
        'token': encoded_jwt
    }, status=HTTP_200_OK)  # returning the token for the future requirments


# method to send the email by generating token for forgot password
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def forgot_password(request):
    to_email = request.data.get("email")  # getting the email from the request
    current_site = get_current_site(request)  # getting the domain
    payload = {
        'email': to_email  # generating the payload
    }

    mail_subject = "forgot password"  # mail subject
    token = jwt.encode(payload, os.getenv('SECRET_KEY_JWT'), algorithm='HS256').decode('utf-8')  # generating the token
    message = render_to_string('FundooApp/forgot_password.html', {
        "domain": current_site,
        "token": token
    })  # redirecting to forgotpassword tempalete and hence reset password
    email = EmailMessage(mail_subject, message, to=[to_email])  # generating the email using EmailMessage class
    email.send()  # sending the email
    return Response({'message': "please do check your email "})


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def reset(request, token):
    email = jwt.decode(token, 'secret')  # decoding the payload
    password = request.data.get("password")  # getting the new password through the request
    password1 = request.data.get("password1")  # checking whether the password entered by the user are same
    try:
        if password == password1:
            serializer_object = CreateUserSerializer()  # creating the object of serializer
            serializer_object.reset_email_password(email, password)  # calling reset email method of serializer
        else:
            raise ValueError("PASSWORDS doesnot match")  # if passwords are not matching raise exception
    except Exception as e:
        return Response({'message': 'reset failed'}, status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["POST"])
def logout(request):
    try:
        redi_obj = redisCreate()
        redi_obj.remove(request.data.get("username"))
        return Response({"message": "Succesful"})
    except Exception as e:
        return Response({"message": e}, status=HTTP_400_BAD_REQUEST)


def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_fileobj(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return response
    return response


@api_view(["POST"])
def upload(request):
    # for uploading the image in the s3 bucket
    try:
        image = request.FILES.get("image")  # getting the image
        res = upload_file(image, 'fundoo-image', 'first_image')  # calling the method for the upload of the file
    except AssertionError as e:
        print("in assertion")
    if res:
        return Response({"message": "success"})
    else:
        return Response({"message": "failed"})


@login_required
def home(request):
    return render(request, 'FundooApp/home.html')


class Note(APIView):
    #  class to do the crud operations in the database
    # serializer_class = NoteSerializer
    def get_object(self,pk):
        try:
            Fundoo_obj=FundooNotes.objects.get(pk=pk)
            return Fundoo_obj
        except FundooNotes.DoesNotExist:
            return Response({'message':'object Not Found'},status=HTTP_404_NOT_FOUND)


    def post(self, request):
        #
        try:
            print('a')
            token_object = services.redisCreate()  # creating the object of the redis cache
            jwt_token = services.redisCreate.get(token_object, 'token')  # retrieving the key
            decode_token = jwt.decode(jwt_token, 'secret')  # decoding the key
            user_id = decode_token['id']  # getting the user id from the key
            Fundoo_user = User.objects.get(id=user_id)  # getting the user from the database
            serializer = NoteSerializer()  # creating the serializer object
            # print('data',str(Note.get(self.user_id)))

            serializer.create(user=Fundoo_user, data=request.data)
            # print(serializer.data)
            # redis_object.hset("FundooNotes", "1", str(serializer.data))
            data = FundooNotes.objects.all().filter(user_id=user_id)
            print("data",data[3])
            print("data", data)
            print(len(data))
            serializer = NoteSerializer(data, many=True)
            print(serializer.data,'11111111111')
            j=0
            for i in serializer.data:
                token_object.hset("funddoonotes","funddoonotes",str(serializer.data))

            print("hai")
            val=token_object.getall("funddoonotes")
            print(type(val))
            print("------------------------------------------------------------------------------------")
            print()
            print(val)
            return Response({'message': 'success'}, status=HTTP_200_OK)
            return Response({'message': 'success'}, status=HTTP_200_OK)
        except Exception as e:
            print('except', e)
            return Response({'message': 'failed'}, status=HTTP_400_BAD_REQUEST)

    def get(self,pk=None):

        redis_object = redisCreate()
        jwt_token = redis_object.get('token')
        decoded_token = jwt.decode(jwt_token, os.getenv('SECRET_KEY_JWT'))
        user_id = decoded_token['id']
        try:
            if user_id is not None:
                if pk is None:  # checking whether
                    data = FundooNotes.objects.all().filter(user_id=user_id)
                    serializer = NoteSerializer(data, many=True)
                    # print("kooi",serializer.data[id])
                    return Response({'hai':serializer.data})
                else:
                    data = FundooNotes.objects.all().filter(user_id=user_id)
                    serializer = NoteSerializer(data)
                    return Response(serializer.data)
            else:
                raise ValueError('user not found')

        except Exception as e:
            print(e)
            return  Response({'message':'someting went wrong'})

    def delete(self, request, pk=None):
        redis_object = redisCreate()
        jwt_token = redis_object.get('token')
        decoded_token = jwt.decode(jwt_token, os.getenv('SECRET_KEY_JWT'))
        user_id = decoded_token['id']
        title =request.data['title']
        try:
           Fundoo_object=FundooNotes.objects.get(title=title)
           if Fundoo_object.user_id ==user_id:
                if pk is None:

                    try:
                        id = FundooNotes.objects.get(title=title)
                        id.delete()
                        return  Response({'message':'delete successful'},status=HTTP_200_OK)
                    except TypeError:
                        FundooNotes.objects.filter(id=id).delete()
                        return Response({'message': 'id not present'})
                    except Exception as e:
                        print(e)
                        return Response({'message': 'id not present'})
                else:
                    try:
                        Fundoo_object = FundooNotes.objects.get(id=pk)
                        if Fundoo_object.user_id == user_id:
                            id = FundooNotes.objects.get(id=pk)
                            id.delete()
                            return Response({'message': 'delete successful'}, status=HTTP_200_OK)
                        else:
                            return Response({'message':'delete unsuccessful user not authorized'})
                    except Exception as e:
                        print(e)
                        return Response({'message':'something went wrong'})
           else:
               return Response({'message':'userid doesnot match'})
        except FundooNotes.DoesNotExist:
            return Response({'message':'value doesnot found'})
        except Exception as e:
            return Response({'message':e})

    # def delete(self,request,pk=None):
    #     redis_object = redisCreate()
    #     jwt_token = redis_object.get('token')
    #     decoded_token = jwt.decode(jwt_token, os.getenv('SECRET_KEY_JWT'))
    #     user_id = decoded_token['id']
    #     try:
    #         print("hai")
    #         title = request.data['title']
    #         # print("olakkasdf", serializer.id)
    #         if pk is None:
    #             print(FundooNotes.user_id)
    #             print(user_id)
    #             if FundooNotes.user_id.filter(title=title)==user_id:
    #                 print("olakka")
    #                 serializer = NoteSerializer()
    #                 serializer.delete(data=request.data)
    #                 return Response({'message':'delete success'},status=HTTP_200_OK)
    #             else:
    #                 return Response({'mesage':'sorry'})
    #         else:
    #             # print("olakka",serializer.id)
    #             if FundooNotes.user_id==user_id:
    #                 print("yes")
    #                 serializer = NoteSerializer()
    #                 serializer.delete(pk=pk)
    #             else:
    #                 print("no")
    #                 return Response({'message':'current user is not a;llowed to delete'})
    #             return Response({'message':'delete success'},status=HTTP_200_OK)
    #
    #     except Exception as e:
    #         return Response({'message':e})

    def put(self,request,pk):
        try:
            redis_object = redisCreate()
            jwt_token = redis_object.get('token')
            decoded_token = jwt.decode(jwt_token, os.getenv('SECRET_KEY_JWT'))
            user_id = decoded_token['id']
            note_object=FundooNotes.objects.get(id=pk)
            if note_object.user_id==user_id:
                if request.data.get('title') is not None:
                    try:
                        note_object.title=request.data.get('title')
                    except Exception as e:
                        print("exception",e)
                if request.data.get('note') is not None:
                    try:
                        note_object.note=request.data.get('note')
                    except Exception as e:
                        print("exception",e)
                if request.data.get('reminder') is not None:
                    try:
                        note_object.reminder=request.data.get('reminder')
                    except Exception as e:
                        print("exception",e)
                if request.data.get('collaborator') is not None:
                    try:
                        note_object.collaborator=request.data.get('collaborator')
                    except Exception as e:
                        print("exception",e)
                if request.data.get('color') is not None:
                    try:
                        note_object.color=request.data.get('color')
                    except Exception as e:
                        print("exception",e)
                if request.data.get('image') is not None:
                    try:
                        note_object.image=request.data.get('image')
                    except Exception as e:
                        print("exception",e)
                if request.data.get('archieve') is not None:
                    try:
                        note_object.archieve=request.data.get('archieve')
                    except Exception as e:
                        print("exception",e)

                note_object.save()

                return Response({'message':'success'},status=HTTP_200_OK)
            else:
                raise ValueError
        except Exception as e:
            print(e)
            return Response({'message':'unsuccess'},status=HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def reminder(request):
    print("inside reminder")
    redis_object = redisCreate()
    jwt_token = redis_object.get('token')
    decoded_token = jwt.decode(jwt_token, os.getenv('SECRET_KEY_JWT'))
    user_id = decoded_token['id']
    note_object = FundooNotes.objects.get(id=FundooNotes.objects.filter(title=request.data.get['title']))
    if note_object.user_id == user_id:
        data = FundooNotes.objects.all().filter(user_id=user_id)
        len_data=len(data)
        for i in range(0,len_data):
            if data[i][reminder] is not None:
                note=data[i]
                print(note)
            return Response({'message':'success'})






    # def put(self,request):
    #     try:
    #         serializer=NoteSerializer()
    #         serializer.update(request)

#
# class Note_pk:
#     def get(self,request,pk):
#         serializer=NoteSerializer()
#         se
def add(request):
    red=redisCreate()
    red.hset("fundoonotes", '1', 'value')
    return HttpResponse('added')
def demo(request):
    redis_obj=redisCreate()
    print(redis_obj.getall("fundoonotes"))
    # return Response({'message':"exapmle"})
    return HttpResponse('DONE')

