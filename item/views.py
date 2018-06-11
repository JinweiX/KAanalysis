from django.shortcuts import render_to_response ,get_object_or_404
from .models import Item,ItemType,ItemSecType
from company.models import Company
from django.shortcuts import redirect

#数据爬虫使用
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

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


def refresh_item(request):
    # 打开浏览器
    driver = webdriver.Chrome()

    # 复制网页操作内容
    base_url_news = "http://zhishu.analysys.cn/public/view/wTopApp/wTopApp.html"

    driver.get(base_url_news)

    #将滚动条拉到最下面
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)

    # 得到网页 html, 还能截图
    html = driver.page_source  # get html
    soup = BeautifulSoup(html, 'lxml')
    columns = soup.find_all('tr')

    columns = columns[:2000]

    for i in range(len(columns) - 1):
        tds = columns[i + 1].find_all('td')

        # tds[0] 当前排名
        #print("排名:", i + 1)

        # tds[1] 名称
        names = tds[1].find_all('a')

        #删除名称中（）中的内容，英文的括号需要转义
        name = names[1].text
        itemName = re.sub('\(.*?\)', '', name)

        # tds[2] 所属行业
        industrys = tds[2].find_all('a')

        # tds[3] 开发商
        companys = tds[3].find_all('a')

        # companyName = companys[0].text
        # if (companyName[:4] == "阿里巴巴"):
        #     print("开发商:阿里巴巴")
        # elif (companyName[3:5] == "腾讯"):
        #     print("开发商:腾讯")
        # else:
        #     print("开发商:", companys[0].text)

        # tds[4] 月活跃用户
        MAU = tds[4].find_all('span')

        # tds[5] 日活跃用户
        DAU = tds[5].find_all('span')


        if not Company.objects.filter(name = companys[0].text).exists():
            Company.objects.create(name = companys[0].text)

        if not ItemType.objects.filter(name = industrys[0].text).exists():
            ItemType.objects.create(name = industrys[0].text)

        if not ItemSecType.objects.filter(name = industrys[1].text).exists():
            ItemSecType.objects.create(name=industrys[1].text,catalog = ItemType.objects.get(name = industrys[0].text))

        if not Item.objects.filter(name = itemName).exists():
            Item.objects.create(name=itemName, company=Company.objects.get(name=companys[0].text),
                        itemType=ItemType.objects.get(name=industrys[0].text), itemSecType=ItemSecType.objects.get(name=industrys[1].text),
                        MAU = float(MAU[0].text.strip().replace(',','').replace('--','0')), DAU = float(DAU[0].text.strip().replace(',','').replace('--','0')) )
        else:
            Item.objects.filter(name = itemName).update(company=Company.objects.get(name=companys[0].text),
                                itemType=ItemType.objects.get(name=industrys[0].text),
                                itemSecType=ItemSecType.objects.get(name=industrys[1].text),
                                MAU=float(MAU[0].text.strip().replace(',','').replace('--','0')), DAU=float(DAU[0].text.strip().replace(',','').replace('--','0')))


    # Item.objects.create(name="测试数据",company=Company.objects.get(name="深圳市腾讯计算机系统有限公司"),
    #                     itemType=ItemType.objects.get(name="社交"), itemSecType=ItemSecType.objects.get(name="社交网络"))
    return redirect('index')

#编辑item的属性
def item_edit(request,item_id):
    content = {}
    item = Item.objects.get(id=item_id)
    content["item"] = item

    return render_to_response('item_edit.html', content)

#更改item状态
def item_update(request,item_id):
    if request.method == "POST":
        state = request.POST.get('state')
        conversion = request.POST.get('conversion')
        Item.objects.filter(id = item_id).update(state = state, conversion = conversion)

    content = {}
    item = Item.objects.get(id=item_id)
    content["item"] = item
    return render_to_response('item_edit.html', content)