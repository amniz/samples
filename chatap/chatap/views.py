from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request): # allows the user for login
    username = request.data.get("username")  # getting the user name
    password = request.data.get("password")  # getting the password
    if username is None or password is None: #  validating
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)  # verifying the user name
    if not user:
        return Response({'error': 'Invalid Credentials'},  # if not found
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)  # if found generating token
    return Response({'token': token.key},
                    status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    try:  # checking for the data is correct or not
        result = {
            "message":"",
            "success": "",
        }
        username=request.data.get("username")  # getting user name and necessary data
        password=request.data.get("password")
        firstname=request.data.get("firstname")
        lastname=request.data.get("lastname")
        email=request.data.get("email")
        if not username:  # error checking whether user name is correct or not
            result['message'] = "Username id required.."
            result['success'] = False
            return Response(result, status=HTTP_400_BAD_REQUEST)  # if user name null the returning a bad request

        if not email:
            if not email:
                result['message'] = "email is  required.."
                result['success'] = False
                return Response(result, status=HTTP_400_BAD_REQUEST)
        if not firstname:
            if not firstname:
                result['message'] = "firstname is  required.."
                result['success'] = False
                return Response(result, status=HTTP_400_BAD_REQUEST)
        if not lastname:
            if not lastname:
                result['message'] = "lastname is  required.."
                result['success'] = False
                return Response(result, status=HTTP_400_BAD_REQUEST)
        if not password:
            if not password:
                result['message'] = "password is  required.."
                result['success'] = False
                return Response(result, status=HTTP_400_BAD_REQUEST)
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email)
        user.set_password(password)  # encrypting the password by hasing
        user.is_active = False  # making is active false untill the email is validated
        user.save()

        # token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': "User Crearted.."},status=HTTP_200_OK)
    except ValueError as e:
        print(e)


