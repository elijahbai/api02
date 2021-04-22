from django.db import models
from django.contrib.auth.models import User,ContentType,Permission
# Create your models here.
class UserToken(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    token = models.CharField(max_length=64,unique=True)
    expiretime = models.IntegerField(verbose_name='到期时间')

    class Meta:
        db_table = 'user_token'

# class ContentTypeExtend(models.Model):
#     contenttype = models.OneToOneField(ContentType, on_delete=models.CASCADE)
#     name = models.CharField(max_length=64)
#     remark = models.CharField(max_length=128, default=None)
#
#     class Meta:
#         db_table = 'content_type_extend'