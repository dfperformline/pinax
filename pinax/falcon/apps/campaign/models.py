from django.db import models
from company.models import Company

# Create your models here.
CAMPAIGN_STATUSES = (
                     ('active','Active'),
                     ('pending','Pending'),
                     ('paused','Paused'),
                     ('dead','Dead'),
                     )

CAMPAIGN_TYPES = (
                  ('email','Email'),
                  ('display','Display'),
                  ('search','Search'),
                  )

class Campaign(models.Model):
    """
    Create a Campaign
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    dt_campaign_id = models.PositiveIntegerField(verbose_name='DirectTrack ID',blank=True)
    status = models.CharField(max_length=30,choices=CAMPAIGN_STATUSES,default='active')
    type = models.CharField(max_length=30,choices=CAMPAIGN_TYPES)
    advertiser = models.ForeignKey(Company)
  
    class Meta:
        permissions = (("manage","Manage"),)
        
    def __unicode__(self):
        return self.name
        
CAMPAIGN_AFFILIATE_STATUSES = (
                  ('active','Active'),
                  ('blocked','Blocked'),
                  )

class CampaignAffiliate(models.Model):
    status = models.CharField(max_length=30,choices=CAMPAIGN_AFFILIATE_STATUSES)
    campaign = models.ForeignKey(Campaign)
    affiliate = models.ForeignKey(Company)
        
    class Meta:
        unique_together = ('campaign','affiliate')
        
    def __unicode__(self):
        return u'%s is %s' % (self.affiliate,self.status)
    
        
class ActionReason(models.Model):
    """
    Pulled from reason_codes
    """
    reason = models.CharField(max_length=255)

    def __unicode__(self):
        return self.reason

class ActionType(models.Model):
    """
    Types of Advertiser actions from advertiser_actions    
    """
    action_type = models.CharField(max_length=30)

    def __unicode__(self):
        return self.action
      
class Action(models.Model):
    type = models.ForeignKey(ActionType)
    reason = models.ForeignKey(ActionReason)
    description = models.TextField()
    #status = models.CharField(max_length=10,choices=('active','archive') 
    sub_id_1 = models.CharField(max_length=255,blank=True)
    sub_id_2 = models.CharField(max_length=255,blank=True)
    sub_id_3 = models.CharField(max_length=255,blank=True)
    sub_id_4 = models.CharField(max_length=255,blank=True)
    #old_payout decimal(10,2) DEFAULT NULL,                        # Previous Payout for campaign/affiliate/subID
    #old_revenue decimal(10,2) DEFAULT NULL,                        # Previous 'revenue?' for campaign/affiliate/subID
    #new_payout decimal(10,2) DEFAULT NULL,                        # New Payout
    #new_revenue decimal(10,2) DEFAULT NULL,                        # New Revenue
    date = models.DateTimeField(auto_now_add=True)
    campaign = models.ForeignKey(Campaign)
    affiliate = models.ForeignKey(Company)

    def __unicode__(self):
        return u'%s on %s' % (self.action,self.date)

