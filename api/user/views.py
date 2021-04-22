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

class LoginView(APIView):
    authentication_classes = []
    def post(self,request,*args,**kwargs):
        print(request.data)
        request = request._request
        print(request)
        if ('username' in request.POST) and ('password' in request.POST):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    # request.session.set_expiry(0)
                    try:
                        token = uuid.uuid1()
                        UserToken.objects.create(user=user,token=token,expiretime=int(time.time()))

                        permission = list(user.get_all_permissions())
                        keys = []
                        for i in range(len(permission)):
                            keys.append(1)

                        return MyResponse.response(data={'token':token, 'permission':dict(zip(permission, keys)),'user_id':user.id})
                    except:
                        return MyResponse.response(code=402)
                        #return MyResponse.response(code=402, msg='请重新登入')
            # return Response({'code': 401, 'status': 'fail', 'msg': '账号或密码错误'})
            return MyResponse.response(code=401, msg='账号或密码错误')
        else:
            # return JsonResponse(code=400,msg='please login')
            return MyResponse.response(code=400, msg='账号或密码错误')

class LogoutView(APIView):
    authentication_classes = []
    def get(self,request,*args, **kwargs):
        token = request.query_params.get('token')
        UserToken.objects.filter(token=token).delete()
        return MyResponse.response()

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

