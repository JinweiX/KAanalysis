from django.db import models
from django.utils import timezone

# 【公司】公司名称、公司市值、上云情况（未上云、腾讯、阿里、其他公司、未知）、公司业务上云占比、上云时间、
# 营收、营收增速、属性（创业/成熟）、公司总部、联系人、联系电话、
class Company(models.Model):
    #公司名称
    name = models.CharField(max_length=50)
    #公司市值
    market_value = models.IntegerField(default = 0)
    #上云情况（未上云、腾讯、阿里、其他公司、未知）
    upCloud = models.CharField(max_length=20,default="未知")
    #云业务占比
    upCloud_percent = models.IntegerField(default=0)
    #上云时间
    upCloud_time = models.DateTimeField(default=timezone.datetime(1111,11,11))
    #投资情况（腾讯系、阿里系、其他、未知）
    invest = models.CharField(max_length=20,default="未知")
    #年收入
    income = models.IntegerField(default=0)
    #年收入增长
    income_increase_rate = models.IntegerField(default=0)
    #公司属性 0-未知  1-创业 2-成熟
    attribute = models.IntegerField(default = 0)
    #公司地址
    location = models.CharField(max_length=10,default="未知")
    #联系人
    contacter = models.CharField(max_length=10,default="未知")
    #联系电话
    contact_phone = models.CharField(max_length=11, default="未知")

    def __str__(self):
        return self.name
