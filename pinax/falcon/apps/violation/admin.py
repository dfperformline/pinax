'''
Created on Jun 30, 2009

@author: adam
'''
from django.contrib import admin
from violation.models import Alert,Flag,Hit

admin.site.register(Alert)
admin.site.register(Flag)
admin.site.register(Hit)
