from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=128,verbose_name='消息')
    user = models.TextField(blank=True, null=True, verbose_name='用户信息')
    class Meta:
        db_table = 'message'