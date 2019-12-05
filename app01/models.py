from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    birth = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)