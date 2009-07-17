from django.db import models

# Create your models here.

class Batch(models.Model):
    """
    Log of batched scripts
    """
    type = models.CharField(max_length=50) 
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()
    status = models.CharField(max_length=4, default="PROC")
    rows_affected = models.PositiveIntegerField()
    server_code = models.CharField(max_length=50,blank=True)
    env_code = models.CharField(max_length=50,blank=True)
    results = models.CharField(max_length=255,blank=True)

    class Meta:
        verbose_name_plural = 'batches'
        
    def __unicode__(self):
        return self.results
    
    
class Message(models.Model):
    """
    Log of messages from apps
    """
    function_code = models.CharField(max_length=10) 
    severity = models.SmallIntegerField() 
    server_code = models.CharField(max_length=50,blank=True)
    env_code = models.CharField(max_length=50,blank=True)
    message = models.CharField(max_length=255,blank=True)
    other = models.CharField(max_length=255,blank=True)
    date = models.DateTimeField(auto_now=True,auto_now_add=True)
    log_batch = models.ForeignKey(Batch)

    def __unicode__(self):
        return self.message