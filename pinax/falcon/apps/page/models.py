from django.db import models
from company.models import Company
from campaign.models import Campaign
from log.models import Batch,Message

# For handling html content as a file
from django.core.files.storage import default_storage as s3_storage
from django.core.files.base import ContentFile
from django.core.cache import cache


# Create your models here.
class Page(models.Model):
    """
    Page process by Transparency
    """
    sub_id_1 = models.CharField(max_length=255,blank=True)
    sub_id_2 = models.CharField(max_length=255,blank=True)
    sub_id_3 = models.CharField(max_length=255,blank=True)
    sub_id_4 = models.CharField(max_length=255,blank=True)
    #image = models.ImageField(upload_to='performline_page_image',blank=True)
    image_url = models.URLField(verify_exists=False)
    content = models.FileField(upload_to='performline_page_source',blank=True)
    content_local = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    affiliate = models.ForeignKey(Company)
    campaign = models.ForeignKey(Campaign)
    score = models.FloatField()

    def __unicode__(self):
        return u'%s' % self.pk

class PageDisplay(Page):
    """
    Detail of page of type display
    """
    url = models.URLField(verify_exists=False,blank=True) 
    referrer = models.URLField(verify_exists=False,blank=True) 
    browser = models.CharField(max_length=255,blank=True)
    platform = models.CharField(max_length=50,blank=True)
    user_agent = models.CharField(max_length=255,blank=True)
    app_version = models.CharField(max_length=30,blank=True)
    app_name = models.CharField(max_length=30,blank=True)
    app_code_name = models.CharField(max_length=30,blank=True)

    def __unicode__(self):
        return self.url
    
class PageEmail(Page):
    """
    Detail of page of type email processed by Transparency
    """
    token = models.PositiveIntegerField()
    header = models.TextField()
    source = models.CharField(max_length=10)
    hash = models.CharField(max_length=255)
    batch = models.ForeignKey(Batch)
    message = models.ForeignKey(Message)

    def __unicode__(self):
        return self.source
    