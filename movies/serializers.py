from rest_framework import serializers

# from django.contrib.auth.models import User

from movies.models import MyUser
from django.core.mail import send_mail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=['username','password','email','first_name','last_name','phone','address']

#to create user account we user uder.objects.create_user not create ,for password hashing
    def create(self,validated_data):
        u=MyUser.objects.create_user(**validated_data)
        u.save()
        send_mail("User Registration Confirmation Mail","your account successfully created","vaishnavivs9605@gmail.com",[u.email,],fail_silently=True)
        return u