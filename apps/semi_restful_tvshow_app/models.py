
from django.db import models

    
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.TextField()
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __repr__(self): 
    #     return f"Show: {self.id} {self.title} ({self.description})"
