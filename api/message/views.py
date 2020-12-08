from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from api.utils.response import MyResponse
from django.contrib.auth import authenticate
from .models import *
import time
import uuid
import json
from .ser import *
from api.utils.pagination import MyPageNumberPagination
from django.conf import settings
#from api.menu.models import EpsMenuGroup
# Create your views here.
# @csrf_exempt
# Create your views here.


class MessageView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            result = Message.objects.all().exclude()
            #result = Message.objects.all().exclude(is_superuser=True)
            pg = MyPageNumberPagination()
            page_queryset = pg.paginate_queryset(queryset=result, request=request, view=self)
            pg.set_index(request,page_queryset)
            ser = MessageSerializer(instance=page_queryset, many=True)
            return MyResponse.response(data=ser.data,count=pg.page.paginator.count)
        else:
            result = Message.objects.get(id=pk)
            ser = MessageSerializer(instance=result, many=False)
            print(ser.data)
        return MyResponse.response(data=ser.data)

    def post(self, request, *args, **kwargs):
        print(request)
        #message = request.data.get('message')
        #password = request.data.get('password')
        try:
            ser = MessageSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return MyResponse.response()
            return MyResponse.response_error(data=ser.errors)
            #Message.objects.create_user(message=message)
        except Exception as e:
            return MyResponse.response_error(code=601,msg='没能添加成功')


    def delete(self,request, *args, **kwargs):
        id = request.data['id']
        #print(self, request, version,pk)
        print(request.data)
        Message.objects.filter(id=id).delete()
        return MyResponse.response()

    def put(self, request,*args, **kwargs):
        print(request)
        try:
            id = request.data['id']
            item = Message.objects.get(id=id)
           # id = request.data['id']
            # username = request.data.get('username')
            #message = request.data.get('message')
            ser = MessageSerializer(data=request.data, instance=item)
            if ser.is_valid():
                ser.save()
                return MyResponse.response()
            return MyResponse.response_error(msg='密码不能为空')
            #mes.set_password(password)
        except Exception as e:
            return MyResponse.response_error(data=e.args[0])


