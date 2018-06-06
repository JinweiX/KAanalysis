from django.contrib import admin
from .models import Item,ItemType,ItemSecType

@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    ordering = ("id",)

@admin.register(ItemSecType)
class ItemSecTypeAdmin(admin.ModelAdmin):
    list_display = ("id","name","catalog")
    ordering = ("id",)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name","company","itemType","itemSecType","MAU","DAU")
    ordering = ("-MAU",)



