from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True 


class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    