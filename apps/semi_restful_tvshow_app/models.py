from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {
        }           # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 1:
            errors["title"] = "Show title name should be at least 1 character"
        if len(postData['network']) < 1:
            errors["network"] = "Show network name should be at least 2 characters"
        if len(postData['release_date']) < 10:
            errors["release_date"] = "Show date name should be at least 10 characters"
        if len(postData['description']) < 2:
            errors["description"] = "Show date name should be at least 2 characters"
        return errors    
        
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.TextField()
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ShowManager()
    

