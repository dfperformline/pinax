'''
Created on Jun 30, 2009

@author: adam
'''
from django.contrib import admin
from company.models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','is_affiliate', 'is_advertiser')
    search_fields = ['name']

admin.site.register(Company,CompanyAdmin)
