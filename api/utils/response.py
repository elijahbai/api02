from rest_framework.response import Response


class MyResponse(object):
    @staticmethod
    def response(code=200, data=None, msg='成功', count=None):
        """
        :param code: 状态码
        :param data: 数据
        :param msg: 提示信息
        :param count: 总条数（分页用）
        :return:
        """
        if count:
            result =  Response({'code': code, 'count':count, 'data': data, 'msg': msg})
        else:
            result =  Response({'code': code, 'data': data, 'msg': msg})
        # result['Access-Control-Allow-Origin'] = "*"  解决跨域
        return result

    @staticmethod
    def response_error(code=500, data=None, msg='失败'):
        """
        :param code: 状态码
        :param data: 数据
        :param msg: 提示信息
        :param count: 总条数（分页用）
        :return:
        """
        return Response({'code': code, 'data': data, 'msg': msg})