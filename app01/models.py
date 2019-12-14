from django.db import models

class MyCharField(models.Field):
    """
    自定义的char类型的字段类
    """

    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(MyCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        """
        限定生成数据库表的字段类型为char，长度为max_length指定的值
        """
        return 'char(%s)' % self.max_length


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    # null=True：数据库中字段是否允许为空；black=True:Admin管理系统中是否允许用户输入为空
    age = models.IntegerField(null=True,blank=True)
    birth = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    phone = MyCharField(max_length=11)


    def __str__(self):
        return '< Person %s-%s>' %(self.id,self.name)