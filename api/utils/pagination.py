from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
from api.utils.response import MyResponse

class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = None

    def get_paginated_response(self, data):
        # print(self.page.number,"@@@",self.page.count(2))
        return MyResponse.response(data=data,count=self.page.paginator.count)
        # return Response(OrderedDict([
        #     ('code',200),
        #     ('count', self.page.paginator.count),
        #     ('next', self.get_next_link()),
        #     ('previous', self.get_previous_link()),
        #     ('data', data)
        # ]))

    def set_index(self,request,page_queryset):
        """添加序号"""
        count = self.get_page_size(request)
        size = self.page.number
        index = (size - 1) * count + 1
        for obj in page_queryset:
            obj.index = index
            index += 1
        pass