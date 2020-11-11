import time
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from api.user.models import UserToken
from django.conf import settings
# from rest_framework.views import exception_handler
from api.utils.response import MyResponse

class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # print(request._request.META)
        now = int(time.time())
        expire_time = now - settings.AUTH_EXPIRE_TIME
        # token = request._request.GET.get('token')
        token = request._request.META.get('HTTP_AUTHORIZATION')
        token_obj = UserToken.objects.filter(token=token,expiretime__gte=expire_time).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed(detail='用户认证失败!')
        token_obj.expiretime = now
        token_obj.save()
        UserToken.objects.filter(expiretime__lt=expire_time).delete()
        return (token_obj.user, token_obj)      # 对应  requset.user, request.auth

    def authenticate_header(self, request):
        pass


def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    # if isinstance(exc, Http404):
    #     exc = exceptions.NotFound()
    # elif isinstance(exc, PermissionDenied):
    #     exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'detail': exc.detail}

        # set_rollback()
        # return Response(data, status=exc.status_code, headers=headers)
        code = exc.status_code * 10
        return MyResponse.response(data=data, code=code)

    return None