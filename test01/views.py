from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from test01.models import User, Article, Person
from django.core import serializers
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from api.utils.pagination import MyPageNumberPagination
from api.utils.response import MyResponse
from .ser import *
from django.shortcuts import render


# Create your views here.

# ok
@csrf_exempt
def my_api(request):
    dic = {}
    if request.method == 'GET':
        dic['message'] = 'hello,ly'
        return HttpResponse(json.dumps(dic))
    else:
        dic['message'] = '方法错误'
        return HttpResponse(json.dumps(dic, ensure_ascii=False))


# ok
@require_http_methods(["GET"])
def add_person(request):
    response = {}
    try:
        person = Person(
            person_name=request.GET.get('person_name'),
            deposit=request.GET.get('deposit')
        )
        person.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# ok
@require_http_methods(["GET"])
def show_persons(request):
    response = {}
    try:
        persons = Person.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", persons))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# post测试
# 定义功能
def add_args(a, b):
    return a + b


# 接口函数
def post(request):
    if request.method == 'POST':  # 当提交表单时
        dic = {}
        # 判断是否传参
        if request.POST:
            a = request.POST.get('a', 0)
            b = request.POST.get('b', 0)
            # 判断参数中是否含有a和b
            if a and b:
                res = add_args(a, b)
                dic['number'] = res
                dic = json.dumps(dic)
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')

    else:
        return HttpResponse('方法错误')


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
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            User.objects.create_user(password=password, username=username)
        except Exception as e:
            return MyResponse.response_error(code=601,msg='用户名不能重复')
        return MyResponse.response()
    def delete(self, request, version,pk):
        User.objects.filter(id=pk).delete()
        return MyResponse.response()

    def put(self, request,  version,pk):
        try:
            user = User.objects.get(id=pk)
            # username = request.data.get('username')
            password = request.data.get('password')
            if not password:
                return MyResponse.response_error(msg='密码不能为空')
            user.set_password(password)
            user.save()
        except Exception as e:
            return MyResponse.response_error(data=e.args[0])
        return MyResponse.response()