from django.db import models

class Info(models.Model):  
    name = models.CharField(max_length=200)  
    pub_date = models.DateTimeField('date published')  
    def __unicode__(self):  
        return self.name      

class Detail(models.Model):  
    info = models.ForeignKey(Info)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)    
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):  
        return self.title      