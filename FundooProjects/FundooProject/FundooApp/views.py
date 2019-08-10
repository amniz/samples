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
from .Serializers import CreateUserSerializer
import os
from .services import redisCreate
from dotenv import load_dotenv, find_dotenv
from pathlib import *
load_dotenv(find_dotenv())
env_path = Path('.')/'.env'

import logging
import boto3
from botocore.exceptions import ClientError
@api_view(["GET"])
def loginsocial(request):

    return render(request,'FundooApp/login.html')

def success(request):
    return render(request,'FundooApp/success.html')


# Create your views here.
# activate view key purpose is to activate the user account using the generated token
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def activate(request, token):
    payload = jwt.decode(token,os.getenv('SECRET_KEY_JWT'))  # decoding the payload from the jwt token
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
        elif  request.POST.get("lastname") is None:
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
        return Response({"message":"duplicate email not allowed"})

    token = jwt.encode(payload,os.getenv('SECRET_KEY_JWT'), algorithm='HS256').decode('utf-8')  # generating the token
    message = render_to_string('FundooApp/account_active_email.html', {
        'domain': current_site.domain,
        'token': token,
    })#generating the message to be send with the email ,rendering the link to account_active_email and giving
                                                                                                    # payload in url
    to_email = serializer.email  # getting the email address
    email = EmailMessage(
        mail_subject, message, to=[to_email]  # creating object of EmailMessage class
    )
    email.send()  # sending the email
    return HttpResponse('Please confirm your email address to complete the registration')

# method used for login of the user by providing username and password
@csrf_exempt
@api_view(["GET","POST"])
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
    encoded_jwt = jwt.encode(payload,os.getenv('SECRET_KEY_JWT'), algorithm='HS256')  # generating the token
    redis_key=redisCreate()  # creating the redis object
    redis_key.set(username,encoded_jwt)  # setting the redis cache key
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
    token = jwt.encode(payload,os.getenv('SECRET_KEY_JWT'), algorithm='HS256').decode('utf-8')  # generating the token
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
    password1 =request.data.get("password1")  # checking whether the password entered by the user are same
    try:
        if password==password1:
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
        redi_obj=redisCreate()
        redi_obj.remove(request.data.get("username"))
        return Response({"message":"Succesful"})
    except Exception as e:
        return Response({"message":e},status=HTTP_400_BAD_REQUEST)

def upload_file(file_name, bucket, object_name=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then same as file_name
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_fileobj(file_name, bucket, object_name )
        except ClientError as e:
            logging.error(e)
            return False
        return True


@api_view(["POST"])
def upload(request):
    print("image",request.data.get("image"))
    try:
        image=request.FILES.get("image")
        print(image,'-----x')
        res=upload_file(image,'fundoo-image','first_image')
    except AssertionError as e:
        print("in assertion")
    if res:
       return Response({"message":"success"})
    else:
        return Response({"message": "success"})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'FundooApp/home.html')

# @csrf_exempt
# def reset(request, token):
#     try:
#         if request.method=='GET':
#             email = jwt.decode(token, 'secret')
#             ser = CreateUserSerializer()
#             user = ser.get_user(email)
#     except(TypeError, ValueError, OverflowError):
#         user = None
#     if user is not None and user.is_active==True:
#         if request.method == "POST":
#             password=request.data['']
#             user.password = password
#             # user.set(password)
#             user.save()
#             return HttpResponse('password reset successful')
#     else:
#         return HttpResponse('Activation link is invalid!')

# method for reset the password of the user who called forgot password method
# @csrf_exempt
# @api_view(["GET","POST"])
# @permission_classes((AllowAny,))
# def reset(request, token):
#     print("in reset")
#     user=None
#     if request.method=='GET':
#         email = jwt.decode(token, 'secret')
#         ser = CreateUserSerializer()
#         user = ser.get_user(email)
#         print("user",user)
#     if request.method=='POST':
#         if user.is_active == True:  # checking whether the user is active or not
#             user.set_password(request.data['password'])  # setting the new password for the user
#             user.save()  # saving the user
        #     return Response({'message': 'reset password succesful'},status=HTTP_200_OK)
        # else:
        #     return Response({"message": "unsuccesful"},HTTP_400_BAD_REQUEST)


    # email = jwt.decode(token, 'secret')  # decoding the payload
    # ser=CreateUserSerializer()
    # user=ser.get_user(email)
    # if user:
    #     if request.method=='POST':
    #         if user.is_active == True:  # checking whether the user is active or not
    #             user.set_password(request.data['password'])  # setting the new password for the user
    #             user.save()  # saving the user
    #             return Response({'message': 'reset password succesful'})
    # else:
    #     return Response({"message":"unsuccesful"})
    # password = request.data.get("password")  # getting the new password through the request
    # password1 =request.data.get("password1")  # checking whether the password entered by the user are same
    # try:
    #     if password==password1:
    #         ser = CreateUserSerializer()  # creating the object of serializer
    #         ser.reset_email_password(email, password)  # calling reset email method of serializer
    #     else:
    #         raise ValueError("PASSWORDS doesnot match")  # if passwords are not matching raise exception
    # except Exception as e:
    #     return Response({'message': 'reset failed'}, status=HTTP_400_BAD_REQUEST)
