from django.db import models

# Create your models here.
class Transaction(models.Model):
    time = models.CharField(max_length=100)
    v1 = models.CharField(max_length=100)
    app_label = 'administrator'
    
    
    
class File(models.Model):
    file = models.FileField(upload_to ="files")
    app_label = 'administrator'