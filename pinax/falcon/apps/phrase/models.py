from django.db import models
from campaign.models import Campaign

LOGIC_CHOICES = (
                 ('banned','banned'),
                 ('expected','expected'),
                 )

class PhraseCategory(models.Model):
    """
    Returns phrase category
    """
    category = models.CharField(max_length=50) 
    description = models.CharField(max_length=255)
    logic = models.CharField(max_length=30,choices=LOGIC_CHOICES)

    class Meta:
        verbose_name_plural = 'phrase categories'
        
    def __unicode__(self):
        return self.name
    
class Phrase(models.Model):
    """
    Returns phrase for Transparency
    """
    phrase = models.CharField(max_length=255)
    logic = models.CharField(max_length=30,choices=LOGIC_CHOICES)
    display = models.BooleanField()
    search = models.BooleanField()
    email = models.BooleanField()
    landing = models.BooleanField()
    campaign = models.ForeignKey(Campaign)
    
    class Meta:
        unique_together = ('phrase','logic','display','search','email','landing','campaign')

    def __unicode__(self):
        return u'%s is %s' % (self.phrase, self.logic)

