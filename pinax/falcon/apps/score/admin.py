'''
Created on Jun 30, 2009

@author: adam
'''
from django.contrib import admin
from score.models import Score,ScoreDetail,ScoreType

admin.site.register(Score)
admin.site.register(ScoreDetail)
admin.site.register(ScoreType)
