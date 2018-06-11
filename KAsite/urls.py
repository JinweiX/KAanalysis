"""KAsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from item.views import item_ka,item_out,index,item_company,item_type,refresh_item,item_edit,item_update

urlpatterns = [
    path('', index, name = "index"),
    path('ka/', item_ka, name = "item_ka"),
    path('out/', item_out, name = "item_out"),
    path('admin/', admin.site.urls),
    path('company_item/<int:company_id>',item_company,name = "item_company"),
    path('type_item/<int:itemType_id>',item_type,name = "item_type"),
    path('refresh_item/',refresh_item,name = "refresh_item"),

    #编辑item
    path('item_edit/<int:item_id>',item_edit,name = "item_edit"),

    #更改item数据
    path('item_update/<int:item_id>',item_update,name = "item_update"),


]
