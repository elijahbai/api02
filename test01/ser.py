from rest_framework import serializers
from django.contrib.auth.models import User,Group
class UserSerializer(serializers.ModelSerializer):
    # company_name = serializers.CharField(source="company.name")
    # status_choices = serializers.ChoiceField(choices='status_choices')
    # status_name = serializers.CharField(source="get_status_display")
    # test = serializers.SerializerMethodField()
    index = serializers.IntegerField(default=1)
    class Meta:
        model = User
        fields = ['id','username','index']
        # fields = "__all__"
        # depth =

    # def get_test(self,obj):
    #     return obj.title

class GroupSerializer(serializers.ModelSerializer):
    # company_name = serializers.CharField(source="company.name")
    # status_choices = serializers.ChoiceField(choices='status_choices')
    # status_name = serializers.CharField(source="get_status_display")
    # test = serializers.SerializerMethodField()
    index = serializers.IntegerField(default=1)
    class Meta:
        model = Group
        fields = ['id','name','index']

class Group2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']