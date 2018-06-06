from django.db import models
from django.contrib.auth.models import User
from company.models import Company

#大行业分类
class ItemType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

#二级行业分类
class ItemSecType(models.Model):
    name = models.CharField(max_length=10)
    catalog = models.ForeignKey(ItemType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

# 【产品】产品名称、公司名称、行业大类、行业细分、月活、日活、行业比重、年营收、
# 营收增速、合作状态（0-未知   1-KA   2-死水）、转化进度（未转化、转化中、已转化）
# 商务、架构师、定级、死水原因、商机推荐
class Item(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete = models.DO_NOTHING)
    itemType = models.ForeignKey(ItemType, on_delete = models.DO_NOTHING)
    itemSecType = models.ForeignKey(ItemSecType , on_delete=models.DO_NOTHING)
    MAU = models.IntegerField(default=0)
    DAU = models.IntegerField(default=0)
    industry_percent = models.IntegerField(default=0)
    #年营收
    income = models.IntegerField(default=0)
    income_rate = models.IntegerField(default=0)
    #合作状态（0-未知   1-KA   2-死水）
    state = models.IntegerField(default=0)
    #转化进度（0-未转化、1-转化中、2-已转化）
    conversion = models.IntegerField(default=0)
    #商务联系人
    business = models.CharField(max_length=30,default="未知")
    #架构师
    architect = models.CharField(max_length=30,default="未知")
    #死水原因
    died_cause = models.TextField(default="未知")
    #是否商机推荐 false-不推荐  true-推荐
    isCommend = models.BooleanField(default=False)

    def __str__(self):
        return "<产品：%s>" % self.name

