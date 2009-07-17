'''
Created on Jul 8, 2009

@author: adam
'''
from django.conf.urls.defaults import *
from page.views import new

urlpatterns = patterns('',
                       url(r'^new', 'page.views.new', name="page_new"),
                       #url(r'^$', 'page.views.all', name="page_list_all"),
)