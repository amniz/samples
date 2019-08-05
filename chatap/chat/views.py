from django.shortcuts import render

# Create your views here.
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
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# def confirm(email):


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

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



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
            result['message'] = "email is  required.."
            result['success'] = False
            return Response(result, status=HTTP_400_BAD_REQUEST)
        if not firstname:
            result['message'] = "firstname is  required.."
            result['success'] = False
            return Response(result, status=HTTP_400_BAD_REQUEST)
        if not lastname:
            result['message'] = "lastname is  required.."
            result['success'] = False
            return Response(result, status=HTTP_400_BAD_REQUEST)
        if not password:
            result['message'] = "password is  required.."
            result['success'] = False
            return Response(result, status=HTTP_400_BAD_REQUEST)
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email)
        user.set_password(password)  # encrypting the password by hasing
        user.is_active = False  # making is active false untill the email is validated
        # activate=confirm(email)
        user.save()
        current_site = get_current_site(request)
        mail_subject = 'Activate your account.'
        message = render_to_string('chat/account_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.id)),
            'token': account_activation_token.make_token(user),
        })
        to_email =request.data.get("email")
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('Please confirm your email address to complete the registration')
    except ValueError as e:
        print(e)


# else:
# form = SignUpForm()
# return render(request, 'accounts/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):

        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


    #
    #     token, _ = Token.objects.get_or_create(user=user)
    #     return Response({'token': "User Crearted.."},status=HTTP_200_OK)
    # except ValueError as e:
    #     print(e)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))

def forgot_password(request):
    email=request.data.get('email')

    user = User.objects.get(email=email)

    if user:
        current_site = get_current_site(request)
        mail_subject = 'password reset'

        # payload ={
        #     "userid":user.pk
        # }
        #
        # token = jwt.encode(payload, 'HELOO', algorithm='HS256')
        message = render_to_string('chat/password_reset.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.id)),
            'token': account_activation_token.make_token(user),
        })
        to_email = request.data.get("email")
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return Response({'Please confirm your email address to change password'}, status=200)
    else:
        return Response({'No such user'}, status=400)



@csrf_exempt
def reset(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        if request.method == "POST":
            password=request.POST.get("password")
            user.password = password
            # user.set(password)
            user.save()
            return HttpResponse('password reset successful')
    else:
        return HttpResponse('Activation link is invalid!')






