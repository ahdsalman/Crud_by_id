from rest_framework import serializers
from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type'},write_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password','password2','is_active']
        # extra_kwargs={
        #     'password':{'write_only':True}
        # }
    def validate(self, data):
        password=data.get('password')
        password2=data.get('password2')
        first_name=data.get('first_name')
        last_name=data.get('last_name')

        if password != password2:
            raise serializers.ValidationError('Password doesn\'t match')
        if first_name !=None:
            if first_name==last_name :
                raise serializers.ValidationError('first_nme and last_name can\'t be same')
        return data
        
    def create(self, validated_data):
          return User.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email','password']


# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         models=User
#         fields = ['first_name','last_name','username']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['email','password']



    