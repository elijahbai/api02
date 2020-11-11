from rest_framework.permissions import BasePermission, DjangoModelPermissions,DjangoObjectPermissions
from django.contrib.auth.models import User,Group
from api.menu.models import EpsMenuGroup, EpsMenu

class MyPermissions(BasePermission):
    def has_permission(self, request, view):
        # print('&&&&&&&&&&&&&&&&',request._request.path)
        # print(request._request.user)
        # user = request._request.user
        # menu_ids = user.groups.all().values("epsmenugroup__menu_id")
        # print(menu_ids)
        # print('----------------')
        # print(dir(view))
        return True
