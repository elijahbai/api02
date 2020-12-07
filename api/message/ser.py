from rest_framework import serializers
from .models import *
class MessageSerializer(serializers.ModelSerializer):
    # company_name = serializers.CharField(source="company.name")
    # status_choices = serializers.ChoiceField(choices='status_choices')
    # status_name = serializers.CharField(source="get_status_display")
    # test = serializers.SerializerMethodField()
    # index = serializers.IntegerField(default=1)
    class Meta:
        model = Message
        fields = ['id','message']
        # fields = "__all__"
        # depth =

    # def get_test(self,obj):
    #     return obj.title

