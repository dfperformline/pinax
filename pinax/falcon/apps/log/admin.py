'''
Created on Jun 30, 2009

@author: adam
'''
from django.contrib import admin
from log.models import Batch,Message

admin.site.register(Batch)
admin.site.register(Message)
