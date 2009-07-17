from django.db import models
from page.models import Page
from campaign.models import Campaign
from company.models import Company

# Create your models here.
IMPRESSION_TYPE_CHOICES = (
                ("affiliate","affiliate"),
                ("advertiser","advertiser"),
                )

class Impression(models.Model):
    """
    Impression information
    """
    sub_id_1 = models.CharField(max_length=255,blank=True)
    sub_id_2 = models.CharField(max_length=255,blank=True)
    sub_id_3 = models.CharField(max_length=255,blank=True)
    sub_id_4 = models.CharField(max_length=255,blank=True)
    datetime = models.DateTimeField() 
    ip = models.IPAddressField(blank=True)
    browser = models.CharField(max_length=255,blank=True)
    type = models.CharField(max_length=30,choices=IMPRESSION_TYPE_CHOICES)
    url = models.URLField(verify_exists=False,blank=True)
    referrer = models.URLField(verify_exists=False,blank=True)
    page = models.ForeignKey(Page) 
    campaign = models.ForeignKey(Campaign)
    affiliate = models.ForeignKey(Company)

    def __unicode__(self):
        return self.url
