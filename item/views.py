from django.shortcuts import render_to_response ,get_object_or_404
from .models import Item,ItemType,ItemSecType
from company.models import Company

def item_ka(request):
    content = {}
    items = Item.objects.filter(state = 1)
    content["items"] = items
    #取前十的公司显示
    companys = Company.objects.all()
    content["companys"] = companys[:10]
    return render_to_response('kaRes.html',content)

def item_out(request):
    content = {}
    items = Item.objects.filter(state = 2)
    content["items"] = items
    #取前十的公司显示
    companys = Company.objects.all()
    content["companys"] = companys[:10]
    return render_to_response('outRes.html', content)

def index(request):
    content = {}
    items = Item.objects.all()
    content["items"] = items

    #取前十的公司显示
    companys = Company.objects.all()
    content["companys"] = companys[:10]

    return render_to_response('index.html',content)

def item_company(requset, company_id):
    content = {}
    items = Item.objects.filter(company_id = company_id)
    content["items"] = items

    company = Company.objects.get(id = company_id)
    content["company"] = company

    # 取前十的公司显示
    companys = Company.objects.all()
    content["companys"] = companys[:10]

    return render_to_response('companyRes.html', content)

def item_type(request, itemType_id):
    content = {}
    items = Item.objects.filter(itemType = itemType_id)
    content["items"] = items

    itemType = ItemType.objects.get(id = itemType_id)
    content["itemType"] = itemType

    # 取前十的公司显示
    companys = Company.objects.all()
    content["companys"] = companys[:10]

    return render_to_response('typeRes.html', content)