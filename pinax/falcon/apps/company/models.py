from django.db import models

# Create your models here.
class Company(models.Model):
    """
    Define company details
    """
    name = models.CharField(max_length=255) 
    direct_track_id = models.CharField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    is_transparency_enabled = models.BooleanField()
    is_transparency_tracked = models.BooleanField(default=True)
    is_affiliate = models.BooleanField()
    is_advertiser = models.BooleanField()
    date_added = models.DateTimeField(auto_now=True,auto_now_add=True)
  
    class Meta:
        permissions = (("manage","Manage"),)
        verbose_name_plural = "companies"

    def __unicode__(self):
        return self.name