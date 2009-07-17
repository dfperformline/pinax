from django.contrib import admin
from campaign.models import Campaign,CampaignAffiliate,ActionReason,ActionType,Action

admin.site.register(Campaign)
admin.site.register(CampaignAffiliate)
admin.site.register(ActionReason)
admin.site.register(ActionType)
admin.site.register(Action)