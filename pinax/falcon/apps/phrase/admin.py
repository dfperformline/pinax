'''
Created on Jun 30, 2009

@author: adam
'''
from django.contrib import admin
from phrase.models import Phrase,PhraseCategory

admin.site.register(Phrase)
admin.site.register(PhraseCategory)
