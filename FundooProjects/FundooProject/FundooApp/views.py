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
from dotenv import load_dotenv, find_dotenv
from pathlib import *
load_dotenv(find_dotenv())
env_path = Path('.')/'.env'

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
    serializer = CreateUserSerializer.create(serializer_object, validated_data=request.data)  # calling the create
                                                 # method to insert data in the User model
    current_site = get_current_site(request)  # getting the current domain address
    mail_subject = 'Activate your account.'  # subject of the mail
    payload = {  # payload to be in included in the token
        'email': serializer.email,
        'username': serializer.username,
        'userid': serializer.id

    }

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
@api_view(["POST"])
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

# method for reset the password of the user who called forgot password method
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def reset(request, token):
    email = jwt.decode(token, 'secret')  # decoding the payload
    password = request.data.get("password")  # getting the new password through the request
    password1 =request.data.get("password1")  # checking whether the password entered by the user are same
    try:
        if password==password1:
            ser = CreateUserSerializer()  # creating the object of serializer
            ser.reset_email_password(email, password)  # calling reset email method of serializer
        else:
            raise ValueError("PASSWORDS doesnot match")  # if passwords are not matching raise exception
    except Exception as e:
        return Response({'message': 'reset failed'}, status=HTTP_400_BAD_REQUEST)
