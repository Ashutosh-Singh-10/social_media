from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from backend import settings
from email.message import  EmailMessage
import random
from datetime import datetime
import pytz
import base64
from base64 import b64decode
from django.core.files.base import ContentFile    
utc=pytz.UTC






def generateImgName():
    
    a='img'+str(random.randint(10000000,99999999))+'.jpg'
    while(len(Post.objects.filter(postImg=a))):
        a='img'+str(random.randint(10000000,99999999))+'.jpg'
    return a
    
def authenticateUser(email,password):
    print(email)
    print(password)
    obj=User.objects.filter(email=email)
    if len(obj)==0 :
        return False
    obj=obj[0]
    if obj.password==password:
        return True
    return False

class SignInView(APIView):
    def post(self,request):
        if "params" in request.data:
            params=request.data["params"]
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if "email" in  params and "password" in params and "Name" in params :
            serializer=User(email=params["email"],password=params["password"],Name=params["Name"])
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
class LoginView(APIView):
    def post(self,request):
        if "params" in request.data:
            params=request.data["params"]
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if "email" in  params and "password" in params :
            if(authenticateUser(params["email"],params["password"])):
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class CreatPostView(APIView):
    def post(self,request):
        if "params" in request.data:
            params=request.data["params"]
        else :
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if "email" in params and "password" in params and "postDesc" in params and  "postImg" in params:
            if not authenticateUser(params["email"],params["password"]) :
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            userObj=User.objects.filter(email=params["email"])[0]
            serializer=Post(postDesc=params["postDesc"],user=userObj)
            image_base64=params["postImg"]
            image_data = b64decode(image_base64)
            
            serializer.postImg = ContentFile(image_data, image_name=generateImgName)
            serializer.save()
            print("everthing is done")
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
   