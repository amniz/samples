#####################################################################################################################
# @author:Muhammed Nisamudheen
# version :{
#               python 3.6
#               django: 2.2
# }
# purpose : Fundoo Application
######################################################################################################################


from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response


# creating a serializer class CreateUserSerializer which uses User Model
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password','first_name','last_name']
        extra_kwargs = {'password': {'write_only': True}}
    #  method to create an database entry in the User model
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],  # getting the email
            username=validated_data['username'],   # getting the username
            first_name=validated_data['firstname'],   # getting the firstname
            last_name=validated_data['lastname']   # getting the lastname
        )
        user.is_active=False  # making the isactive field to False
        user.set_password(validated_data['password'])  # setting the password for the user by hashing
        user.save()  # saving the user in the data base
        return user

    #  method to activate the user
    def validate(self,id,email):
        user=User.objects.get(id=id)  # getting the user through the id
        try:
            if user.is_active==False:   # checking whether user is active
                user.is_active=True  # making useractive to true for login purposes
                user.save()  # saving the user
                return Response({'message':'UserACTIVATED'})
            else:
                raise ValueError
        except ValueError:
            print("not valid")
    # method to reset the password of the user
    def reset_email_password(self,email,password):
        valide_mail=email['email']  # getting the email of the user
        try:
            user = User.objects.get(email=valide_mail)  # getting the user from the email

            if user.is_active==True:  # checking whether the user is active or not
                user.set_password(password)  # setting the new password for the user
                user.save()  # saving the user
                return Response({'message':'reset password succesful'})

        except User.DoesNotExist:
            return Response({'message': 'reset password not succesful'})

