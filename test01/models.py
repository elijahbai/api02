from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=50)
    upwd = models.CharField(max_length=100)
    #active inactive
    status = models.CharField(max_length=10)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    #deleted alive
    status = models.CharField(max_length=10)


class Person(models.Model):
    person_name = models.CharField('姓名', max_length=64, null=False)
    deposit = models.FloatField('存款')
    add_time = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.person_name, self.deposit