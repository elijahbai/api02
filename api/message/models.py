from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=128,unique=True,verbose_name='消息')

    class Meta:
        db_table = 'message'