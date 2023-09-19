from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAdminUser
# Create your views here.


class RegisterView(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(request,email=email,password=password)
            if user is not None:
                return Response({'Msg':'Login successful'},status=status.HTTP_200_OK)
            
            else:
                return Response({'Msg':'Datas not Valid'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ProfileView(APIView):
    def get(self,request,pk):
        # request.user
        try:
            user=User.objects.get(id=pk)
            serializer=RegisterSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"Msg":'User not found'},status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,pk):
        try:
            user=User.objects.get(id=pk)
            serializer=RegisterSerializer(user,data=request.data,partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'User not found'})
        
    def delete(self,request,pk):
        try:
            user=User.objects.get(id=pk)
            user.delete()
            return Response({'Msg':'Data Deleted'})
        except User.DoesNotExist:
            return Response('User Not Found')



class UserView(APIView):
    def get(self,request,pk):
        try:
            user=User.objects.get(id=pk)
            if user.is_admin:
                users=User.objects.filter(is_admin=False)
                serializer=RegisterSerializer(users,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response({'View Only For Admin'})
        except User.DoesNotExist:
            return Response({'Msg':'User not Found'})
    



        


         
