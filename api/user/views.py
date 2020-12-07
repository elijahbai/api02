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


class UserView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            result = User.objects.all().exclude(is_superuser=True)
            pg = MyPageNumberPagination()
            page_queryset = pg.paginate_queryset(queryset=result, request=request, view=self)
            pg.set_index(request,page_queryset)
            ser = UserSerializer(instance=page_queryset, many=True)
            return MyResponse.response(data=ser.data,count=pg.page.paginator.count)
        else:
            result = User.objects.get(id=pk)
            ser = UserSerializer(instance=result, many=False)
        return MyResponse.response(data=ser.data)

    def post(self, request, *args, **kwargs):
        print(request)
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            User.objects.create_user(password=password, username=username)
        except Exception as e:
            return MyResponse.response_error(code=601,msg='用户名不能重复')
        return MyResponse.response()

    def delete(self,request, *args, **kwargs):
        id = request.data['id']
        #print(self, request, version,pk)
        print(request.data)
        User.objects.filter(id=id).delete()
        return MyResponse.response()

    def put(self, request,*args, **kwargs):
        try:
            id = request.data['id']
            user = User.objects.get(id=id)
            # username = request.data.get('username')
            password = request.data.get('password')
            if not password:
                return MyResponse.response_error(msg='密码不能为空')
            user.set_password(password)
            user.save()
        except Exception as e:
            return MyResponse.response_error(data=e.args[0])
        return MyResponse.response()
