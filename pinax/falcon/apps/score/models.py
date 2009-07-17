from django.db import models
from phrase.models import Phrase



class ScoreType(models.Model):
    """
    Types of score weights
    """
    #affiliate
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=255)
    weight = models.FloatField() 

    def __unicode__(self):
        return self.name
    
    
class Score(models.Model):
    """
    Score page
    """
    score = models.FloatField() 
    #flag tinyint(1) unsigned DEFAULT NULL
    #status varchar(30)  DEFAULT 'pending'
    #review varchar(30)  DEFAULT 'not reviewed'
    date = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(ScoreType)

    def __unicode__(self):
        return u'%s' % self.score

class ScoreDetail(models.Model):
    """
    Detail page processed by Transparency
    """
    #line_number int(11) DEFAULT NULL
    #line_source text
    date = models.DateTimeField(auto_now_add=True)
    phrase = models.ForeignKey(Phrase)
    score = models.ForeignKey(Score)

    def __unicode__(self):
        return u'%s on %s' % (self.phrase, self.date)

    