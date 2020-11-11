from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from test01.models import User,Article,Person
from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
# Create your views here.


@csrf_exempt
def my_api(request):
    dic = {}
    if request.method == 'GET':
        dic['message'] = 'hello,ly'
        return HttpResponse(json.dumps(dic))
    else:
        dic['message'] = '方法错误'
        return HttpResponse(json.dumps(dic, ensure_ascii=False))


#新增文章

def add_article(request):
    if request.method == "POST":
        print(request)
        print("test")
        req =json.loads(request.body)
        #req = json.loads(request.body)
        #print(req)
        key_flag = req.get("title") and req.get("content") and len(req)==2
        #判断请求体是否正确
        if key_flag:
            title = req["title"]
            content = req["content"]
            #title返回的是一个list
            title_exist = Article.objects.filter(title=title)
            #判断是否存在同名title
            if len(title_exist) != 0:
                return JsonResponse({"status":"BS.400","msg":"title aleady exist,fail to publish."})
            '''插入数据'''
            add_art = Article(title=title,content=content,status="alive")
            add_art.save()
            return JsonResponse({"status":"BS.200","msg":"publish article sucess."})
        else:
            return  JsonResponse({"status":"BS.400","message":"please check param."})
    else:
        return  JsonResponse({"status":"BS.400","message":"please check param."})

#修改文章

def modify_article(request,art_id):
    if request.method == "POST":
        req = json.loads(request.body.decode())
        try:
            art = Article.objects.get(id=art_id)
            key_flag = req.get("title") and req.get("content") and len(req)==2
            if key_flag:
                title = req["title"]
                content = req["content"]
                title_exist = Article.objects.filter(title=title)
                if len(title_exist) > 1:
                    return JsonResponse({"status":"BS.400","msg":"title aleady exist."})
                '''更新数据'''
                old_art = Article.objects.get(id=art_id)
                old_art.title = title
                old_art.content = content
                old_art.save()
                return JsonResponse({"status":"BS.200","msg":"modify article sucess."})
        except Article.DoesNotExist:
            return  JsonResponse({"status":"BS.300","msg":"article is not exists,fail to modify."})
        # 删除文章
    else:
        return JsonResponse({"status": "BS.300", "msg": "article is not exists,fail to modify."})


        # if request.method == "DELETE":
        #     try:
        #         # art = Article.objects.get(id=art_id)
        #         # art_id = art.id
        #         # art.delete()
        #         print("test")
        #         return JsonResponse({"status": "BS.200", "msg": "delete article sucess."})
        #     except Article.DoesNotExist:
        #         return JsonResponse({"status": "BS.300", "msg": "article is not exists,fail to delete."})


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