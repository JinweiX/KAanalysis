from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name","upCloud","market_value","attribute","location")
    ordering = ("-market_value",)


