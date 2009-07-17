'''
Created on Jun 30, 2009

@author: adam
'''
from django.contrib import admin
from page.models import PageEmail,PageDisplay

admin.site.register(PageEmail)
admin.site.register(PageDisplay)
