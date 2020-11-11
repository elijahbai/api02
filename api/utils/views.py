from rest_framework.views import APIView
from django.http import JsonResponse
from api.utils.response import MyResponse
import requests
from django.core.files.uploadedfile import InMemoryUploadedFile

class MyView(APIView):
    HOST = ''
    SERVICE_NAME = ''
    SCHEME = 'http'
    def get_url_parts(self,path):
        # print(path)
        # try:
        #     # url_parts = self.URL_MAP[self.__class__.__name__]
        #     index = path.find(self.SERVICE_NAME)
        #     return path[index+len(self.SERVICE_NAME)+1:]
        # except:
        #     return None
        return path
    def get_headers(self,request):
        headers = {
        }
        for k, v in request._request.headers.items():
            if k == 'Accept' or k == 'Content-Type':
                continue
            headers[k] = v
        return headers
    def get_data_files(self,request):
        files = {}
        data = {}
        for item in request.data:
            # print(type(item))
            if type(request.data[item]) is InMemoryUploadedFile:
                files[item] = (request.data[item].name, request.data[item].file.read())
            else:
                data[item] = request.data[item]
        return data,files
    def get_response(self,response):
        response['host'] = self.HOST
        return response

    def get(self,request,*args,**kwargs):
        try:
            url_parts = self.get_url_parts(request._request.path)
            if not url_parts:
                return MyResponse.response_error(msg='没找到对应配置')
            headers = self.get_headers(request)
            url = "%s://%s%s" %(self.SCHEME,self.HOST,url_parts)
            response = requests.get(url,params=request.query_params,headers=headers)
            # response = json.loads(response.text)
            response = self.get_response(response.json())
            return JsonResponse(response)
        except Exception as e:
            return MyResponse.response_error(data=e.args)
    def post(self,request,*args,**kwargs):
        try:
            url_parts = self.get_url_parts(request._request.path)
            if not url_parts:
                return MyResponse.response_error(msg='没找到对应配置')
            headers = self.get_headers(request)
            data, files = self.get_data_files(request)
            url = "%s://%s%s" % (self.SCHEME, self.HOST, url_parts)
            response = requests.post(url,data=data,files=files,params=request.query_params,headers=headers)
            response = self.get_response(response.json())
            return JsonResponse(response)
        except Exception as e:
            return MyResponse.response_error(data=e.args)

    def put(self,request,*args,**kwargs):
        try:
            url_parts = self.get_url_parts(request._request.path)
            if not url_parts:
                return MyResponse.response_error(msg='没找到对应配置')
            headers = self.get_headers(request)
            data,files = self.get_data_files(request)
            url = "%s://%s%s" % (self.SCHEME, self.HOST, url_parts)
            response = requests.put(url, data=data,files=files, params=request.query_params, headers=headers)
            response = self.get_response(response.json())
            return JsonResponse(response)
        except Exception as e:
            return MyResponse.response_error(data=e.args)

    def delete(self,request,*args,**kwargs):
        try:
            url_parts = self.get_url_parts(request._request.path)
            if not url_parts:
                return MyResponse.response_error(msg='没找到对应配置')
            headers = self.get_headers(request)
            url = "%s://%s%s" % (self.SCHEME, self.HOST, url_parts)
            response = requests.delete(url, data=request.data, params=request.query_params, headers=headers)
            # response = json.loads(response.text)
            return JsonResponse(response.json())
        except Exception as e:
            return MyResponse.response_error(data=e.args)